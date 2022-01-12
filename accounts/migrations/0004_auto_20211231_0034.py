# Generated by Django 3.2.9 on 2021-12-30 19:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211229_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='programs_bought',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='programs_created',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
    ]