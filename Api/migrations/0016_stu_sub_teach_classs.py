# Generated by Django 4.0.4 on 2022-04-18 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0015_remove_student_quiz_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Requirments', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=70)),
                ('subject_taught', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Classs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.teach')),
                ('student_id', models.ManyToManyField(to='Api.stu')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.sub')),
            ],
        ),
    ]
