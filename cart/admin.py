from django.contrib import admin
from .models import Item, Order, OrderItem, Payment
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
