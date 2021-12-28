# Generated by Django 3.2.9 on 2021-12-28 18:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211229_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='programs_bought',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=None),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='programs_created',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=None),
        ),
    ]
