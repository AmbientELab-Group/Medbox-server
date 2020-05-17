# Generated by Django 2.2.12 on 2020-05-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CRT', 'Caretaker'), ('DR', 'Doctor')], default='CRT', max_length=3),
        ),
    ]