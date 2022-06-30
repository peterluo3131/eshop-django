# Generated by Django 4.0.5 on 2022-06-30 12:35

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryitem',
            options={'verbose_name': 'Item category', 'verbose_name_plural': 'Item categories'},
        ),
        migrations.AlterModelOptions(
            name='itemimage',
            options={'verbose_name': 'Titelbild', 'verbose_name_plural': 'Titelbild'},
        ),
        migrations.AlterField(
            model_name='item',
            name='delivery_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Lieferpreis'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title_image',
            field=models.ImageField(upload_to=core.models.item_image_path, verbose_name='Titelbild'),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(upload_to=core.models.item_image_path, verbose_name='Titelbild'),
        ),
    ]
