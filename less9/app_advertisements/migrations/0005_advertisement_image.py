# Generated by Django 4.2.2 on 2023-08-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0004_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='advertisements/', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]
