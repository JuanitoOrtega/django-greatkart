# Generated by Django 3.1 on 2022-12-24 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=255, verbose_name='ID de carrito')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Carrito',
                'verbose_name_plural': 'Carritos',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart', verbose_name='Carrito')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Producto')),
                ('variations', models.ManyToManyField(blank=True, to='store.Variation', verbose_name='Variación')),
            ],
            options={
                'verbose_name': 'Artículo de carrito',
                'verbose_name_plural': 'Artículos de carrito',
            },
        ),
    ]
