# Generated by Django 3.1 on 2022-12-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_reviewrating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewrating',
            options={'verbose_name': 'Reseña', 'verbose_name_plural': 'Reseñas'},
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='review',
            field=models.TextField(max_length=500, verbose_name='Reseña'),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Asunto'),
        ),
    ]