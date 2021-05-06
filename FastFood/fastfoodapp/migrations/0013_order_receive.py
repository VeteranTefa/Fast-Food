# Generated by Django 3.0.5 on 2021-04-23 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0012_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='fastfoodapp.Customer')),
                ('Delivery_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='fastfoodapp.DeliveryInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='fastfoodapp.Customer')),
                ('Food_it_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='fastfoodapp.FoodItem')),
            ],
        ),
    ]
