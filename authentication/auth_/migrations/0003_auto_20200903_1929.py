# Generated by Django 3.1.1 on 2020-09-03 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0002_auto_20200902_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='full_name',
            new_name='name',
        ),
    ]