# Generated by Django 4.0.4 on 2022-04-25 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_alter_companies_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='company_name',
            field=models.SlugField(verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='company_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.companies'),
        ),
    ]
