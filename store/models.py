from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class BrandManager(models.Manager):
    def get_queryset(self):
        return super(BrandManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(
        _("Category Name"),
        max_length=255,
        db_index=True,
    )
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = _("categories")

    def get_absolute_url(self):
        return reverse(
            'store:category_list',
            args=[self.slug]
        )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        _("Brand Name"),
        max_length=255,
        db_index=True,
    )
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(
        _("Brand Visibility"),
        default=True,
    )
    objects = models.Manager()
    brands = BrandManager()

    def get_absolute_url(self):
        return reverse(
            'store:brand_list',
            args=[self.slug]
        )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='product', null=True, on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(
        Brand, related_name='brand', null=True, on_delete=models.SET_NULL
    )
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(
        verbose_name=_("Product Name"),
        help_text=_("Title"),
        max_length=255
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Product Description"),
        blank=True,
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        help_text=_("Select Image"),
        upload_to="images/",
        default="images/600_900.png",
    )
    buying_price = models.PositiveIntegerField(
        _("Buying Price"),
        default=0,
    )
    regular_price = models.PositiveBigIntegerField(
        _("Regular Price"),
        default=0,
    )
    sale_price = models.PositiveBigIntegerField(
        verbose_name=_("Discounted Price"),
        help_text=_("Price On Sale"),
        default=0,
    )
    quantity = models.IntegerField(
        verbose_name=_("Quantity"),
        help_text=("Stock"),
        default=1,
    )
    wieght = models.DecimalField(
        verbose_name=_("Product Weight"),
        help_text=_("Weight in Gram"),
        default=0, max_digits=6, decimal_places=2
    )
    in_stock = models.BooleanField(_("Stock Availability"),
                                   default=True,
                                   )
    is_active = models.BooleanField(
        _("Product Visibility"),
        default=True,
    )
    created = models.DateTimeField(
        _("Create At"),
        auto_now_add=True,
        editable=False,
    )
    updated = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
    )
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse(
            'store:product_detail',
            args=[self.slug]
        )

    def __str__(self):
        return self.title
