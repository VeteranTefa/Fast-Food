# Generated by Django 3.0.5 on 2021-04-23 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0009_deliveryinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='has',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Delivery_id', models.ForeignKey(default=201, on_delete=django.db.models.deletion.SET_DEFAULT, to='fastfoodapp.DeliveryInfo')),
                ('Food_it_id', models.ForeignKey(default=101, on_delete=django.db.models.deletion.SET_DEFAULT, to='fastfoodapp.FoodItem')),
            ],
        ),
    ]
