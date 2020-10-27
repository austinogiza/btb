from django.urls import include, path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add_one/<slug>/', views.add_one_to_cart, name="add_one"),
    path('add_five/<slug>/', views.add_five_to_cart, name="add_five"),
    path('add_ten/<slug>/', views.add_ten_to_cart, name="add_ten"),
    path('add_twenty/<slug>/', views.add_twenty_to_cart, name="add_twenty"),
    path('add_fifty/<slug>/', views.add_fifty_to_cart, name="add_fifty"),


]
