# Generated by Django 4.1.4 on 2023-02-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=25)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
