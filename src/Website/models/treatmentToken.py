"""
Model of the token for importing treatment.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020"

from django.db import models
from .treatment import Treatment

class TreatmentToken(models.Model):
    """
    Token for assigning treatment to the user.
    """
    # token for importing treatment
    token = models.CharField(max_length=16, unique=True)
    
    # reference to the treatment
    treatment = models.ForeignKey(Treatment, on_delete=models.PROTECT)
    
    # expiration date for the key
    expires = models.DateTimeField()
