# Generated by Django 5.0.6 on 2024-05-23 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cross_asistent', '0012_articulos_encabezado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tareas',
            name='proyecto',
        ),
        migrations.DeleteModel(
            name='proyectos',
        ),
        migrations.DeleteModel(
            name='tareas',
        ),
    ]