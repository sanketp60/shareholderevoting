# Generated by Django 3.2 on 2021-05-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20210502_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='Company',
            field=models.CharField(max_length=50),
        ),
    ]