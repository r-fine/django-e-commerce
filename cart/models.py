from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import IntegerField
from store.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.title
