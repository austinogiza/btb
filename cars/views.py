from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView
from .forms import ContactForm, CustomSignupForm
from .models import Contact
# Create your views here.

def home(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        message = form.cleaned_data.get('message')

        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        contact.save()
        return redirect('btb:contact-success')

    context = {
        'form':form
    }
    return render(request, 'contact.html', context)

def contact_success(request):
    return render(request, 'contact-success.html')



class SignUp(CreateView):
    form_class = CustomSignupForm
    template_name = 'account/signup.html'
    success_url = '/'