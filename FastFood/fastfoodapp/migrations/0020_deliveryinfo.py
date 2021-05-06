# Generated by Django 3.0.5 on 2021-04-24 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0019_auto_20210424_0349'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_Name', models.CharField(max_length=200)),
                ('D_time', models.DateTimeField()),
                ('D_totalCost', models.FloatField()),
            ],
        ),
    ]
