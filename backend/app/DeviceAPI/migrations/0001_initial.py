# Generated by Django 3.0 on 2020-09-01 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerVersion',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('capacity', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceVersion',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('capacity', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('pairingKey', models.CharField(default='', max_length=6)),
                ('pairingKeyExpiresAt', models.DateTimeField(null=True)),
                ('apiToken', models.CharField(default='', max_length=42)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ownedDevices', to=settings.AUTH_USER_MODEL)),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='devices', to='DeviceAPI.DeviceVersion')),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('lastRefill', models.DateTimeField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='containers', to='DeviceAPI.Device')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='containers', to='DeviceAPI.ContainerVersion')),
            ],
        ),
        migrations.CreateModel(
            name='Chamber',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('isFull', models.BooleanField(default=False)),
                ('realAdministrationTime', models.DateTimeField(blank=True, null=True)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chambers', to='DeviceAPI.Container')),
            ],
        ),
    ]