# Generated by Django 3.2.18 on 2023-05-17 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0240_auto_20230512_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='rsa_pubkey',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='MediumKeySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('public_id', models.IntegerField(unique=True)),
                ('media_type', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('uid_key', models.BinaryField()),
                ('diversification_key', models.BinaryField()),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medium_key_sets', to='pretixbase.organizer')),
            ],
        ),
        migrations.AddConstraint(
            model_name='mediumkeyset',
            constraint=models.UniqueConstraint(condition=models.Q(('active', True)), fields=('organizer', 'media_type'), name='keyset_unique_active'),
        ),
    ]