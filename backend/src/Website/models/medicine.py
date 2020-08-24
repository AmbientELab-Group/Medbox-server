"""
Model of the medicine.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.db import models

class Medicine(models.Model):
    """
    Model of the medicine.
    """
    # name of the medicine
    name = models.CharField(max_length=500) 
