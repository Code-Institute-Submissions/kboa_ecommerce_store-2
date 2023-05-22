from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from profiles.models import UserProfile
from wishlist.models import Wishlist
from products.models import Product


# Create your views here.


def view_wishlist(request):
    """ A view to return the wishlist/saved items """
    redirect_url = request.META.get('HTTP_REFERER')

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return redirect(redirect_url)
    else:
        return redirect(redirect_url)

    wishlist_product_ids = Wishlist.objects.filter(user_profile=profile).values_list("product_id", flat=True)
    products = Product.objects.filter(id__in=list(wishlist_product_ids))

    context = {
        "products": products,
    }

    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, product_id):
    """ Add a product to the wishlist """
    redirect_url = request.META.get('HTTP_REFERER')

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return redirect(redirect_url)
    else:
        return redirect(redirect_url)

    product = get_object_or_404(Product, pk=product_id)
    try:
        wishlist = Wishlist.objects.get(user_profile=profile, product=product)
    except Wishlist.DoesNotExist:
        wishlist = None

    if wishlist:
        wishlist.delete()
        messages.info(request, f'Remove {product.name} from wishlist')
    else:
        wishlist = Wishlist(user_profile=profile, product=product)
        wishlist.save()
        messages.info(request, f'Added {product.name} to your wishlist')

    return redirect(redirect_url)
