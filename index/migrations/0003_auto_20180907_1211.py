# Generated by Django 2.1.1 on 2018-09-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180905_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uage',
            field=models.IntegerField(),
        ),
    ]
