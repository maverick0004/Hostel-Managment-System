# Generated by Django 2.0.1 on 2018-05-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0004_auto_20180522_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='caretaker',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='warden',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
