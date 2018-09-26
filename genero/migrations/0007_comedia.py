# Generated by Django 2.1 on 2018-08-21 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genero', '0006_auto_20180817_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.CharField(max_length=60)),
                ('nota', models.PositiveSmallIntegerField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='midia')),
            ],
            options={
                'verbose_name_plural': 'Comédias',
            },
        ),
    ]
