# Generated by Django 3.0 on 2020-09-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]