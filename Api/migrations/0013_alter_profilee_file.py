# Generated by Django 4.0.4 on 2022-04-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0012_alter_profilee_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilee',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]