# Generated by Django 2.2.6 on 2019-10-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refashion', '0004_auto_20191020_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_number',
            field=models.PositiveSmallIntegerField(default=69203),
        ),
    ]