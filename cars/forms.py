from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser, Contact
from django_countries.fields import CountryField
from django_countries import countries, Countries
from django_countries.widgets import CountrySelectWidget

COUNTRY_CHOICES = tuple(countries)

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "First Name"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Last Name"
    }))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "placeholder": "Phone Number"
    }))
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=True,widget=CountrySelectWidget(attrs={

        "class": "form-select"
    }))

    class Meta:
        model = CustomUser
        fields = ('__all__')

    def signup(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data.get['first_name']
        user.last_name = self.cleaned_data.get['last_name']     
        user.phone = self.cleaned_data.get['phone']
        user.country = self.cleaned_data.get['country']
        user.save()
   

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "placeholder": "Full Name",
        "class": 'form-input'
    }))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "placeholder": "Email",
        "class": 'form-input'
    }))
    phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "placeholder": "Your Phone",
        "class": 'form-input'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Your Message",
        "class": 'form-textarea'

    }))
    


