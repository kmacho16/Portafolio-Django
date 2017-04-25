# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio_app', '0007_prueba'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cat', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='proyectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proy', models.CharField(max_length=100)),
                ('descripcion_corta', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField()),
                ('web_site', models.CharField(blank=True, max_length=100)),
                ('mi_cat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Proy_cat', to='portafolio_app.categorias')),
            ],
        ),
        migrations.RemoveField(
            model_name='prueba',
            name='prueba',
        ),
        migrations.DeleteModel(
            name='prueba',
        ),
    ]