# Generated by Django 4.2.5 on 2023-09-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_rename_users_appusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='appusers',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='appusers',
            name='lastaname',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='appusers',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
