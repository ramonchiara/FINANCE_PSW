# Generated by Django 4.2.3 on 2023-07-05 19:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('extrato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='valores',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valores',
            name='descricao',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]