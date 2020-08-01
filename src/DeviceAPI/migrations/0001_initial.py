# Generated by Django 3.0 on 2020-05-25 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('serialNumber', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DevicePairingKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=6)),
                ('expires', models.DateTimeField()),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='DeviceAPI.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceApiToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=42)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='DeviceAPI.Device')),
            ],
        ),
    ]