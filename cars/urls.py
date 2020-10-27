from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page

app_name = 'btb'

urlpatterns = [

    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name="contact-success"),
    path('price/', views.CarsView.as_view(), name="cars"),


]
