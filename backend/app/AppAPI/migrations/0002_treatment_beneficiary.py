# Generated by Django 3.0 on 2020-12-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='beneficiary',
            field=models.CharField(default='Johnny', max_length=100),
            preserve_default=False,
        ),
    ]