# Generated by Django 5.0.6 on 2024-05-16 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross_asistent', '0007_banners_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banners',
            name='articulo',
            field=models.URLField(default='un_articulo.com'),
        ),
    ]
