# Generated by Django 5.0.1 on 2024-01-19 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='store',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='store',
            name='whatsapp',
            field=models.URLField(blank=True, null=True, verbose_name='Whatsapp'),
        ),
        migrations.AlterField(
            model_name='store',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True, verbose_name='CNPJ'),
        ),
    ]
