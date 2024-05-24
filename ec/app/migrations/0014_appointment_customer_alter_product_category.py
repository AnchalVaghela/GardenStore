# Generated by Django 4.1.4 on 2023-03-09 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_product_composition_remove_product_prodapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PL', 'Plants'), ('T', 'Tools'), ('FE', 'Fertilizers'), ('DCP', 'Disease'), ('FL', 'Flowers'), ('P', 'Pots')], max_length=5),
        ),
    ]
