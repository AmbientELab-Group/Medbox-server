# Generated by Django 2.2.12 on 2020-05-23 13:37

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdherenceTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.TimeField()),
                ('isPredefined', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineDosing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doses', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('emergency', models.BooleanField(default=False)),
                ('takenFrom', models.DateField()),
                ('takenTo', models.DateField(blank=True, null=True)),
                ('adherenceTimes', models.ManyToManyField(to='Website.AdherenceTime')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Website.Medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxDeviation', models.IntegerField(blank=True, null=True)),
                ('patientFirstName', models.CharField(max_length=30)),
                ('patientLastName', models.CharField(max_length=150)),
                ('caretaker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('medicines', models.ManyToManyField(to='Website.MedicineDosing')),
                ('predefinedTimes', models.ManyToManyField(to='Website.AdherenceTime')),
            ],
        ),
    ]
