# Generated by Django 3.0.5 on 2021-04-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0044_auto_20210428_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='R_Area',
            field=models.CharField(default='Qena', max_length=200),
        ),
    ]
