# Generated by Django 3.1 on 2022-09-09 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220908_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(null=True, verbose_name='Cantidad en mano'),
        ),
    ]
