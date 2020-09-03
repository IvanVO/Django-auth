# Generated by Django 3.0.8 on 2020-09-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
