# Generated by Django 3.2 on 2021-05-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='DateOfBirth',
            field=models.DateField(),
        ),
    ]