# Generated by Django 4.1.4 on 2024-03-29 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_remove_datechoice_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DateChoice',
        ),
    ]
