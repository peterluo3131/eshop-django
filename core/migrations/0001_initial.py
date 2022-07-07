# Generated by Django 4.0.6 on 2022-07-07 13:33

import autoslug.fields
import common.models
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=common.models.carousel_image_path)),
                ('title', models.CharField(max_length=120, verbose_name='Name')),
                ('body', models.TextField(verbose_name='Hauptteil')),
                ('alt', models.TextField(verbose_name='Alt text')),
                ('index', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Carousel',
                'verbose_name_plural': 'Carousels',
            },
        ),
        migrations.CreateModel(
            name='CategoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('id',))),
            ],
            options={
                'verbose_name': 'Item category',
                'verbose_name_plural': 'Item categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('id',))),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preis')),
                ('delivery_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Lieferpreis')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Rabatt')),
                ('label', models.CharField(blank=True, choices=[('n', 'NEW'), ('h', 'HOT')], max_length=1, null=True)),
                ('stock', models.PositiveIntegerField(default='1', verbose_name='Lager')),
                ('title_image', models.ImageField(upload_to=common.models.item_image_path, verbose_name='Titelbild')),
                ('item_video', embed_video.fields.EmbedVideoField(blank=True, verbose_name='Item video')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('additional_information', models.TextField(blank=True, null=True, verbose_name='Zusätzliche Information')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Erstellungsdatum')),
                ('ordered_counter', models.PositiveIntegerField(default='0', verbose_name='Bestellt Zähler')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.categoryitem', verbose_name='Kategorie')),
            ],
            options={
                'verbose_name': 'Artikel',
                'verbose_name_plural': 'Artikeln',
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=common.models.item_image_path, verbose_name='Titelbild')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.item')),
            ],
            options={
                'verbose_name': 'Titelbild',
                'verbose_name_plural': 'Titelbild',
            },
        ),
    ]
