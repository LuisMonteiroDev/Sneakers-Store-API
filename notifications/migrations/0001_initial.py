# Generated by Django 5.0.1 on 2024-02-10 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(verbose_name='Titulo')),
                ('message', models.TextField(max_length=255, verbose_name='Mensagem')),
                ('is_read', models.BooleanField(default=False, verbose_name='Foi lida')),
                ('send_date', models.DateTimeField(verbose_name='Data de envio')),
            ],
            options={
                'verbose_name': 'Notificação',
                'verbose_name_plural': 'Notificações',
            },
        ),
    ]
