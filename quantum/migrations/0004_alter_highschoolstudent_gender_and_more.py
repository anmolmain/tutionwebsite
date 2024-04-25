# Generated by Django 5.0.4 on 2024-04-24 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantum', '0003_highschoolstudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highschoolstudent',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6),
        ),
        migrations.AlterField(
            model_name='middleschoolstudent',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6),
        ),
        migrations.AlterField(
            model_name='middleschoolstudent',
            name='interests',
            field=models.TextField(blank=True, null=True),
        ),
    ]