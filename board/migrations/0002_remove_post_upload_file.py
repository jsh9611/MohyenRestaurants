# Generated by Django 3.2.9 on 2021-12-12 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload_file',
        ),
    ]