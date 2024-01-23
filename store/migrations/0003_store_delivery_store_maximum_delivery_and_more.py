# Generated by Django 5.0.1 on 2024-01-22 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_store_email_store_facebook_store_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='delivery',
            field=models.BooleanField(default=False, verbose_name='Faz entrega'),
        ),
        migrations.AddField(
            model_name='store',
            name='maximum_delivery',
            field=models.IntegerField(blank=True, default=60, null=True, verbose_name='Tempo máximo de entrega'),
        ),
        migrations.AddField(
            model_name='store',
            name='minimum_delivery',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tempo minímo de entrega'),
        ),
    ]
