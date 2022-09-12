from django.db import models
from store.models import Product, Variation

# Create your models here.
class Cart(models.Model):
  cart_id = models.CharField(max_length=255, blank=True, verbose_name='ID de carrito')
  date_added = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

  class Meta:
    verbose_name = 'Carrito'
    verbose_name_plural = 'Carritos'

  def __str__(self):
    return self.cart_id

class CartItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
  variations = models.ManyToManyField(Variation, blank=True, verbose_name='Variación')
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Carrito')
  quantity = models.IntegerField(verbose_name='Cantidad')
  is_active = models.BooleanField(default=True, verbose_name='Activo')

  class Meta:
    verbose_name = 'Artículo'
    verbose_name_plural = 'Artículos'

  def sub_total(self):
    return self.product.price * self.quantity

  def __unicode__(self):
    return self.product