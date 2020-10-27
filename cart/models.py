from django.db import models
from ckeditor.fields import RichTextField
from cars.models import CustomUser
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    description = RichTextField()
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_add_one(self):
        return reverse('cart:add_one', kwargs={
            'slug': self.slug
        })

    def get_add_five(self):
        return reverse('cart:add_five', kwargs={
            'slug': self.slug
        })

    def get_add_ten(self):
        return reverse('cart:add_ten', kwargs={
            'slug': self.slug
        })

    def get_add_twenty(self):
        return reverse('cart:add_twenty', kwargs={
            'slug': self.slug
        })

    def get_add_fifty(self):
        return reverse('cart:add_fifty', kwargs={
            'slug': self.slug
        })

    # def get_price(self):
    #     return "{:.2f}".format(self.price / 100)


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(pre_save_product_receiver, sender=Item)


class OrderItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    # order = models.ForeignKey(
    #     "Order", related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} x {self.item.title}"

    def get_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    created_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER - {self.pk}"

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_price()
        return total


class Payment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    amount = models.FloatField()
    reference = models.CharField(max_length=300)

    def __str__(self):
        return self.order
