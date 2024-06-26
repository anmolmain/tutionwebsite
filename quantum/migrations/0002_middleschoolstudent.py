# Generated by Django 5.0.4 on 2024-04-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiddleSchoolStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('current_class', models.CharField(choices=[('fourthGrade', 'Fourth Grade'), ('fifthGrade', 'Fifth Grade'), ('sixthGrade', 'Sixth Grade'), ('seventhGrade', 'Seventh Grade'), ('eighthGrade', 'Eighth Grade')], max_length=20)),
                ('parent_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('emergency_contact', models.CharField(max_length=15)),
                ('subjects_required', models.TextField()),
                ('academic_goals', models.TextField()),
                ('interests', models.TextField()),
            ],
        ),
    ]
