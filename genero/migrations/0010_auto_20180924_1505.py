# Generated by Django 2.1 on 2018-09-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genero', '0009_auto_20180918_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animacao',
            name='nota',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
