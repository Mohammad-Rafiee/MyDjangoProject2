# Generated by Django 4.0.4 on 2022-04-25 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_alter_devices_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.companies'),
        ),
    ]
