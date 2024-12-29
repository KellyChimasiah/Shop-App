from django.shortcuts import render,get_object_or_404
from shop.models import Item
from django.db.models import Q
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def shop(request):
    query = request.GET.get('gsearch', '')  # Use 'gsearch' to match the form's input name
    if query:
        items = Item.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) | 
            Q(price__icontains=query)
        )
    else:
        items = Item.objects.all()
    return render(request, 'index.html', {'items': items, 'query': query})
# def shop(request):
#     query= request.GET.get('q')
#     if query:
#         items=Item.objects.filter(
#             Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query)
#         )
#     else:
#         items=Item.objects.all()
#         return render(request, 'index.html', {'items':items})
    
   
    

def about(request,item_id):
    item=get_object_or_404(Item, id=item_id)
    return render(request,'about.html', {'item':item})

# contact form
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send the email
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['chimasiahindeche@gmail.com'],
                fail_silently=False,
            )

            # Render success page
            return render(request, 'contact_success.html', {'name': name})
    else:
        form = ContactForm()  # Initialize an empty form for GET requests

    # Render the contact form (for both GET and invalid POST cases)
    return render(request, 'contact.html', {'form': form})