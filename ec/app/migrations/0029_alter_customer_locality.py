# Generated by Django 4.1.4 on 2023-03-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_customer_locality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='locality',
            field=models.CharField(max_length=200),
        ),
    ]
