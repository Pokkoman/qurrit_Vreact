# Generated by Django 3.2.9 on 2021-11-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_altexerciselist_alt_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='trainer_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
