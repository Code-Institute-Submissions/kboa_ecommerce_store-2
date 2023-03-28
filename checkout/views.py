from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MW06wDHLVYaCninCs35YJ7ttM3yqrJbnVuy4XpEUMUuj7djWGUEet2KjzYMsbOx8Nlds8jkQeyD0W1X08bgFxQZ00vSWQcWLw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
