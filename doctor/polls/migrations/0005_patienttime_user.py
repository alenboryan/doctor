# Generated by Django 4.1.4 on 2024-03-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_patienttime_user_doctor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienttime',
            name='user',
            field=models.ManyToManyField(to='polls.doctor'),
        ),
    ]
