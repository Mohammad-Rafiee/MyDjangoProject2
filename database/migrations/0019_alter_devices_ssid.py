# Generated by Django 4.0.4 on 2022-06-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_alter_devices_ssid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='ssid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
