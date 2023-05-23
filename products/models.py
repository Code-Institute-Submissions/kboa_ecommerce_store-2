from django.conf import settings
from django.db import models
from profiles.models import UserProfile
from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)

    def __str__(self):
        return self.name


class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    recommended_product = models.ForeignKey(Product, related_name='related_products', on_delete=models.CASCADE)

    def __str__(self):
        return self.recommended_product.name


class Review(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=0,)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
