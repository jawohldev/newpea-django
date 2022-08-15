# Generated by Django 4.0.3 on 2022-07-19 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=200)),
                ('Subject', models.CharField(max_length=200)),
                ('CustomerEmail', models.CharField(max_length=200)),
                ('Message', models.CharField(max_length=4096)),
                ('Timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeName', models.CharField(max_length=200)),
                ('EmployeeEmail', models.CharField(max_length=200)),
            ],
        ),
    ]
