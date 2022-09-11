# Generated by Django 3.1 on 2022-09-11 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20220910_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_category', models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100, verbose_name='Tipo de variación')),
                ('variation_value', models.CharField(max_length=100, verbose_name='Opciones')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Variación')),
            ],
        ),
    ]
