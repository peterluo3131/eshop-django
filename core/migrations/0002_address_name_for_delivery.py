# Generated by Django 3.2 on 2021-08-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='name_for_delivery',
            field=models.CharField(default='John', max_length=120),
            preserve_default=False,
        ),
    ]