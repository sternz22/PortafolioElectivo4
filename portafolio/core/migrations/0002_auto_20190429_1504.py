# Generated by Django 2.0.2 on 2019-04-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='home',
            name='under_title',
            field=models.CharField(max_length=200, verbose_name='Sub Título'),
        ),
    ]
