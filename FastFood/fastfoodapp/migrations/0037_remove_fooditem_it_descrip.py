# Generated by Django 3.1.7 on 2021-04-26 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0036_auto_20210426_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='It_Descrip',
        ),
    ]
