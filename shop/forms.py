from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=50 , required=True , widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    message=forms.CharField(required=True,  widget=forms.Textarea(attrs={'class':'form-control'}))


    def __str__(self):
        return self.name
    