# Generated by Django 5.0.1 on 2024-01-07 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0003_alter_photonasa_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photonasa',
            name='image',
            field=models.ImageField(default=None, upload_to='static/image/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
