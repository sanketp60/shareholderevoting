# Generated by Django 3.2 on 2021-05-03 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('poll', '0004_alter_poll_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('UserID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('Pan', models.CharField(max_length=10)),
                ('DateOfBirth', models.DateTimeField()),
            ],
        ),
    ]