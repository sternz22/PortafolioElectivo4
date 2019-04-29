# Generated by Django 2.0.2 on 2019-04-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190429_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleAbout', models.CharField(max_length=200, verbose_name='Título')),
                ('nameAbout', models.CharField(max_length=200, verbose_name='Nombre')),
                ('headerAbout', models.CharField(max_length=200, verbose_name='Cabeza')),
                ('descriptionAbout', models.TextField(verbose_name='Descripción')),
                ('under_titleAbout', models.CharField(max_length=200, verbose_name='Sub Título')),
                ('imageAbout', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
                'ordering': ['-created'],
            },
        ),
    ]