# Generated by Django 5.0.1 on 2024-02-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_privacypolicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacypolicy',
            name='privacy_policy',
            field=models.FileField(upload_to='privacy_police/', verbose_name='Politica de Privacidade'),
        ),
        migrations.AlterField(
            model_name='termsofuse',
            name='terms',
            field=models.FileField(upload_to='terms_of_use/', verbose_name='Termos de Uso'),
        ),
    ]
