# Generated by Django 3.2.9 on 2022-01-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211231_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='wallet',
            field=models.IntegerField(default=0),
        ),
    ]
