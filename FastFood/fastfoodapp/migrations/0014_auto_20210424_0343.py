# Generated by Django 3.0.5 on 2021-04-24 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0013_order_receive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add',
            name='F_id',
        ),
        migrations.RemoveField(
            model_name='has',
            name='Food_it_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Food_it_id',
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
    ]
