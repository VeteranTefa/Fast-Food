# Generated by Django 3.0.5 on 2021-04-28 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0046_auto_20210428_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='F_Images',
            field=models.ImageField(default='media/images/null.png', upload_to='media/images'),
        ),
    ]
