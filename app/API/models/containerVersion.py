from django.db import models


class ContainerVersion(models.Model):
    # name of the version eg. 1.0
    name = models.CharField(
        primary_key=True,
        max_length=8
    )

    # max number of containers fitting to this version of device
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name}"
