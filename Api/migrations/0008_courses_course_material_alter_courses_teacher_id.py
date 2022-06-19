# Generated by Django 4.0.4 on 2022-04-17 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0007_remove_quiz_class_name_student_quiz_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_material',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.teacher'),
        ),
    ]