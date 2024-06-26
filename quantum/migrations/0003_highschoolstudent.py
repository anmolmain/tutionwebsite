# Generated by Django 5.0.4 on 2024-04-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantum', '0002_middleschoolstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighSchoolStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('current_class', models.CharField(choices=[('ninthGrade', 'Ninth Grade'), ('tenthGrade', 'Tenth Grade'), ('eleventhGrade', '10+1 Grade'), ('twelfthGrade', '10+2 Grade'), ('spokenEnglish', 'Spoken English')], max_length=20)),
                ('parent_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('emergency_contact', models.CharField(max_length=15)),
                ('subjects_required', models.TextField()),
                ('interests', models.TextField(blank=True, null=True)),
                ('expectations', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
