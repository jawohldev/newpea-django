# Generated by Django 4.1 on 2022-08-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmgmt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='CustomerName',
            new_name='CompanyName',
        ),
        migrations.AddField(
            model_name='contactform',
            name='CustomerFirstName',
            field=models.CharField(default='None', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactform',
            name='CustomerLastName',
            field=models.CharField(default='None', max_length=200),
            preserve_default=False,
        ),
    ]
