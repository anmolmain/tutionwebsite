# Generated by Django 5.0.4 on 2024-04-25 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quantum', '0007_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_at',
        ),
    ]