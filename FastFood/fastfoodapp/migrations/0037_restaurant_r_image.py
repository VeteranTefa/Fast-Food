# Generated by Django 3.1.7 on 2021-04-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0036_auto_20210427_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='R_Image',
            field=models.ImageField(default='null', upload_to='media/images'),
        ),
    ]
