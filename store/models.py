from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class BrandManager(models.Manager):
    def get_queryset(self):
        return super(BrandManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    brands = BrandManager()

    def get_absolute_url(self):
        return reverse('store:brand_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand, related_name='brand', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/600_900.png')
    price = models.PositiveIntegerField(default=0)
    wieght = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
