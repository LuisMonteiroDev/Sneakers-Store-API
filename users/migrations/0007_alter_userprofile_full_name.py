# Generated by Django 5.0.1 on 2024-01-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_userprofile_type_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome completo'),
        ),
    ]
