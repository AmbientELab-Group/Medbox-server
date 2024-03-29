from django.db import models
from API.models.chamber import Chamber


class ContainerManager(models.Manager):
    def create_with_chambers(self, **container_data):
        """
        Creates container and associated chambers.
        """
        container = self.create(**container_data)
        for pos in range(container_data.get("version").capacity):
            Chamber.objects.create(container=container, position=pos)

        return container
