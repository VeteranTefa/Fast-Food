# Generated by Django 3.1.7 on 2021-04-26 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0033_remove_restaurant_r_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditem',
            old_name='F_Images',
            new_name='f_images',
        ),
    ]
