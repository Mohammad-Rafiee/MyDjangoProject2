# Generated by Django 4.0.4 on 2022-05-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_devices_broker_ip_devices_gateway_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='device_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='ID'),
        ),
    ]