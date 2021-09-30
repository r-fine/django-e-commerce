from django.db import models
from store.models import Product
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
    )


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
