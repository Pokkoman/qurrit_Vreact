# Generated by Django 3.2.9 on 2022-01-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220125_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
