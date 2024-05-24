# Generated by Django 4.1.4 on 2023-02-20 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_alter_appointment_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
        migrations.AddField(
            model_name='appointment',
            name='guser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('Landscaping', 'Landscaping'), ('Lawn Care', 'Lawn care')], default='Doctor care', max_length=50),
        ),
    ]
