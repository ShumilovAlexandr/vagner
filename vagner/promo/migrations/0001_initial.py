# Generated by Django 5.0.1 on 2024-01-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoNasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название фото')),
                ('image', models.ImageField(default=None, upload_to='image/%Y/%m/%d/', verbose_name='Фото')),
            ],
        ),
    ]