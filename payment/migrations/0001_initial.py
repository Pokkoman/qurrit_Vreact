# Generated by Django 3.2.9 on 2022-01-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=200)),
                ('program_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]