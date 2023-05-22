from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from coupon.models import Coupon


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    discount = 0
    cart = request.session.get('cart', {})
    coupon_id = request.session.get('coupon_id')
    discount_code = None
    coupon = None

    if (coupon_id):
        coupon = Coupon.objects.get(id=coupon_id)

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    sub_total = total

    if coupon:
        discount_code = coupon.code
        discount = sub_total * Decimal(coupon.discount / 100)
        if (discount > sub_total):
            discount = sub_total
        sub_total = sub_total - discount

    grand_total = sub_total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'sub_total': sub_total,
        'discount': discount,
        'discount_code': discount_code,
        'coupon': coupon,
    }

    return context
