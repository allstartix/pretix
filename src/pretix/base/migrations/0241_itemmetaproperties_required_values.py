# Generated by Django 3.2.19 on 2023-05-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0240_auto_20230516_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmetaproperty',
            name='allowed_values',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='itemmetaproperty',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]