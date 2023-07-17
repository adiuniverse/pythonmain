# Generated by Django 4.1.4 on 2023-01-30 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('education', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
