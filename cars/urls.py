from django.urls import path, include
from . import views

app_name = 'btb'

urlpatterns = [

    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name="contact-success")
    
]
