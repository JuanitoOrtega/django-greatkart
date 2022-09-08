# Generated by Django 3.1 on 2022-09-08 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True, verbose_name='Categoría')),
                ('slug', models.CharField(max_length=200, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, upload_to='photos/categories', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
    ]
