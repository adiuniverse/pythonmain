# Generated by Django 4.1.4 on 2023-02-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0005_addstudent_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudentbatch',
            name='b_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]