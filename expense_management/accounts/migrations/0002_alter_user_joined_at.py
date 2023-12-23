# Generated by Django 5.0 on 2023-12-23 00:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='joined date'),
        ),
    ]
