# Generated by Django 4.1.4 on 2023-03-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_customer_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='locality',
            field=models.CharField(max_length=200),
        ),
    ]
