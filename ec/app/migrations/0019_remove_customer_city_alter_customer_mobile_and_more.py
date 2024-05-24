# Generated by Django 4.1.4 on 2023-03-24 07:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_customer_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.PositiveIntegerField(),
        ),
    ]
