# Generated by Django 2.0.2 on 2019-04-29 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Títulos'),
        ),
    ]