# Generated by Django 3.1 on 2022-09-09 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_auto_20220908_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, unique=True, verbose_name='Producto')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio')),
                ('images', models.ImageField(upload_to='photos/products', verbose_name='Galería')),
                ('stock', models.IntegerField(blank=True, verbose_name='Cantidad en mano')),
                ('is_available', models.BooleanField(default=True, verbose_name='Disponible')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Categoría')),
            ],
        ),
    ]
