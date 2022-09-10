from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=50, unique=True, verbose_name='Categoría')
  slug = models.SlugField(max_length=200, unique=True)
  description = models.TextField(max_length=255, blank=True, verbose_name='Descripción')
  image = models.ImageField(upload_to='photos/categories', blank=True, verbose_name='Imagen')

  class Meta:
    verbose_name = 'Categoría'
    verbose_name_plural = 'Categorías'

  def get_url(self):
    return reverse('products_by_category', args=[self.slug])

  def __str__(self):
    return self.category_name
