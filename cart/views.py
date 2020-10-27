from django.shortcuts import render, get_object_or_404, redirect
from .utils import get_or_set_order_session
from .models import Order, OrderItem, Item
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def add_one_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order_item.quantity >= 100:
            messages.info(
                request, 'You have reached the maximum permitted quantity of 100 tickets')
        else:
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 1
                order_item.save()
            else:
                order.items.add(order_item)
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.add(order_item)
    return redirect('btb:cars')


def add_five_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order_item.quantity >= 100:
            messages.info(
                request, 'You have reached the maximum permitted quantity of 100 tickets')
        else:
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 5
                order_item.save()
            else:
                order.items.add(order_item)
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.add(order_item)
    return redirect('btb:cars')


def add_ten_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order_item.quantity >= 100:
            messages.info(
                request, 'You have reached the maximum permitted quantity of 100 tickets')
        else:
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 10
                order_item.save()
            else:
                order.items.add(order_item)
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.add(order_item)
    return redirect('btb:cars')


def add_twenty_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order_item.quantity >= 100:
            messages.info(
                request, 'You have reached the maximum permitted quantity of 100 tickets')
        else:
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 20
                order_item.save()
            else:
                order.items.add(order_item)
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.add(order_item)
    return redirect('btb:cars')


def add_fifty_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order_item.quantity >= 100:
            messages.info(
                request, 'You have reached the maximum permitted quantity of 100 tickets')
        else:
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 50
                order_item.save()
            else:
                order.items.add(order_item)
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.add(order_item)
    return redirect('btb:cars')
