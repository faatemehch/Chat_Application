# Generated by Django 3.2.9 on 2021-11-23 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='message',
        ),
    ]