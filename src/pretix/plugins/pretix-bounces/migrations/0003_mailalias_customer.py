# Generated by Django 3.2.3 on 2021-05-21 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0188_delete_requiredaction'),
        ('pretix_bounces', '0002_auto_20190830_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailalias',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.customer'),
        ),
    ]
