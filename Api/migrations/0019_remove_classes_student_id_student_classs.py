# Generated by Django 4.0.4 on 2022-04-21 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0018_quiz_file_alter_courses_file_classes_quiz_classs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='student_id',
        ),
        migrations.AddField(
            model_name='student',
            name='classs',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='Api.classes'),
            preserve_default=False,
        ),
    ]