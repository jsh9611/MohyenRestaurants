# Generated by Django 3.2.9 on 2021-12-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_rename_trashcans_restaurants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
