# Generated by Django 4.0.4 on 2022-04-15 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_studentcourses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentcourses',
            old_name='course_name',
            new_name='class_name',
        ),
    ]
