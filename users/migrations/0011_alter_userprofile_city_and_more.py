# Generated by Django 5.0.1 on 2024-03-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_userprofile_cep_userprofile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='number_house',
            field=models.CharField(default='', verbose_name='Número da casa'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(default='', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='street',
            field=models.CharField(default='', verbose_name='Rua'),
        ),
    ]
