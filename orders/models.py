from django.db import models
from accounts.models import User
from store.models import Product, Variation
from django_countries.fields import CountryField


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    payment_id = models.CharField(max_length=100, verbose_name='ID de pago')
    payment_method = models.CharField(max_length=100, verbose_name='Método de pago')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto de pago')
    status = models.CharField(max_length=100, verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return self.payment_id


class Order(models.Model):
    STATUS = (
        ('New', 'Nuevo'),
        ('Accepted', 'Aceptado'),
        ('Completed', 'Completado'),
        ('Cancelled', 'Cancelado'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Usuario')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Pago')
    order_number = models.CharField(max_length=20, verbose_name='Número de pedido')
    first_name = models.CharField(max_length=50, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    phone = models.CharField(max_length=15, verbose_name='Teléfono')
    email = models.EmailField(max_length=50, verbose_name='Correo electrónico')
    address_line_1 = models.CharField(max_length=50, verbose_name='Dirección línea 1')
    address_line_2 = models.CharField(max_length=50, blank=True, verbose_name='Dirección línea 2')
    country = CountryField(blank_label='Seleccionar país', verbose_name='País')
    state = models.CharField(max_length=50, verbose_name='Estado/Región')
    city = models.CharField(max_length=50, verbose_name='Ciudad')
    order_note = models.CharField(max_length=100, blank=True, verbose_name='Nota de pedido')
    order_total = models.FloatField(verbose_name='Total pedido')
    tax = models.FloatField(verbose_name='Impuesto')
    status = models.CharField(max_length=10, choices=STATUS, default='New', verbose_name='Estado del pedido')
    ip = models.CharField(blank=True, max_length=20, verbose_name='Dirección IP')
    is_ordered = models.BooleanField(default=False, verbose_name='Pedido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def __str__(self):
        return self.first_name


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Pedido')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Pago')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    variations = models.ManyToManyField(Variation, blank=True, verbose_name='Variaciones')
    quantity = models.IntegerField(verbose_name='Cantidad')
    product_price = models.FloatField(verbose_name='Precio del producto')
    ordered = models.BooleanField(default=False, verbose_name='Pedido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Producto pedido'
        verbose_name_plural = 'Productos pedidos'

    def __str__(self):
        return self.product.product_name