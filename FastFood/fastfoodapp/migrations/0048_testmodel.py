# Generated by Django 3.1.7 on 2021-04-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoodapp', '0047_auto_20210428_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('Mid', models.AutoField(primary_key=True, serialize=False)),
                ('MName', models.CharField(max_length=50)),
            ],
        ),
    ]
