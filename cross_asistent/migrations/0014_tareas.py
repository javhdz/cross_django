# Generated by Django 5.0.6 on 2024-05-23 21:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross_asistent', '0013_remove_tareas_proyecto_delete_proyectos_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.CharField(max_length=255)),
                ('importante', models.BooleanField(default=False)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('completado', models.DateTimeField(null=True)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
