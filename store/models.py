from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
  product_name = models.CharField(max_length=255, unique=True, verbose_name='Producto')
  slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
  description = models.TextField(max_length=500, blank=True, verbose_name='Descripción')
  old_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Precio anterior')
  price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Precio')
  images = models.ImageField(upload_to='photos/products', verbose_name='Galería')
  stock = models.IntegerField(blank=True, null=True, verbose_name='Cantidad en mano')
  is_available = models.BooleanField(default=True, verbose_name='Disponible')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

  class Meta:
    verbose_name = 'Producto'
    verbose_name_plural = 'Productos'

  def get_url(self):
    return reverse('product_detail', args=[self.category.slug, self.slug])

  def __str__(self):
    return self.product_name