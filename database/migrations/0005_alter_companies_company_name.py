# Generated by Django 4.0.4 on 2022-04-17 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_devices_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='company_name',
            field=models.CharField(max_length=50),
        ),
    ]
