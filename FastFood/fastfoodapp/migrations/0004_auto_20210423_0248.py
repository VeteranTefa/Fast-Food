# Generated by Django 3.0.5 on 2021-04-23 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0003_auto_20210423_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_Name', models.CharField(max_length=200)),
                ('R_Type', models.CharField(max_length=200)),
                ('R_Email', models.EmailField(max_length=254)),
                ('R_Password', models.CharField(max_length=200)),
                ('R_City', models.CharField(max_length=200)),
                ('R_Area', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='custcontact',
            name='Customer_id',
        ),
        migrations.RemoveField(
            model_name='has',
            name='Delivery_id',
        ),
        migrations.RemoveField(
            model_name='has',
            name='Food_it_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Customer_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Food_it_id',
        ),
        migrations.RemoveField(
            model_name='receive',
            name='Customer_id',
        ),
        migrations.RemoveField(
            model_name='receive',
            name='Delivery_id',
        ),
        migrations.DeleteModel(
            name='Add',
        ),
        migrations.DeleteModel(
            name='CustContact',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='DeliveryInfo',
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
        migrations.DeleteModel(
            name='has',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Receive',
        ),
    ]
