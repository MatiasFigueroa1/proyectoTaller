# Generated by Django 4.2.7 on 2023-11-27 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='teléfono',
        ),
    ]
