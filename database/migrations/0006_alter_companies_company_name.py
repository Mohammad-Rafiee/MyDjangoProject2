# Generated by Django 4.0.4 on 2022-04-17 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_alter_companies_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='company_name',
            field=models.SlugField(),
        ),
    ]