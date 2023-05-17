from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='wishlist')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item
