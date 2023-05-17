# Generated by Django 3.2.18 on 2023-05-12 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0239_giftcard_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='giftcardacceptance',
            old_name='collector',
            new_name='acceptor',
        ),
        migrations.AddField(
            model_name='giftcardacceptance',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='giftcardacceptance',
            name='reusable_media',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='giftcardacceptance',
            name='issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_card_acceptor_acceptance', to='pretixbase.organizer'),
        ),
        migrations.AlterUniqueTogether(
            name='giftcardacceptance',
            unique_together={('issuer', 'acceptor')},
        ),
    ]