from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import User
from django.db.models import Avg, Count


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

    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

    def __str__(self):
        return self.product_name


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


variation_category_choice = (
    ('color', 'Color'),
    ('size', 'Talla'),
)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    variation_category = models.CharField(max_length=100, choices=variation_category_choice, verbose_name='Tipo de variación')
    variation_value = models.CharField(max_length=100, verbose_name='Variación')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Variación'
        verbose_name_plural = 'Variaciones'

    objects = VariationManager()

    def __str__(self):
        return self.variation_value


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    subject = models.CharField(max_length=100, verbose_name='Asunto')
    review = models.TextField(max_length=500, verbose_name='Reseña')
    rating = models.FloatField(verbose_name='Calificación')
    ip = models.CharField(max_length=20, blank=True, verbose_name='Dirección IP')
    status = models.BooleanField(default=True, verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualización')

    class Meta:
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'

    def __str__(self):
        return self.subject


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, verbose_name='Producto')
    image = models.ImageField(upload_to='store/products', verbose_name='Imagen')

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'

    def __str__(self):
        return self.product.product_name