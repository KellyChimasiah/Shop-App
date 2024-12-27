from django.shortcuts import render,get_object_or_404
from shop.models import Item
from django.db.models import Q

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

