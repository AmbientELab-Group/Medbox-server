"""
Model of the treatment.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "20.5.2020" 

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import models
from .medicine import Medicine

class AdherenceTime(models.Model):
    """
    Model of the adherence time.
    """
    # optional name for the time, used for defining times
    name = models.CharField(max_length=100, blank=True, null=True)
    
    # time
    time = models.TimeField()
    
    # is the time predefined
    isPredefined = models.BooleanField(default=False)

class MedicineDosing(models.Model):
    """
    Medicine dosing profile.
    """
    # medicine that we want to dose
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)

    # time's associated with the medicine
    adherenceTimes = models.ManyToManyField(AdherenceTime)
    
    # number of pills per dose
    doses = ArrayField(models.IntegerField())
    
    # is medicine only taken in case of some event
    emergency = models.BooleanField(default=False)
    
    # date from which the user starts to take the medicine
    takenFrom = models.DateField()
    
    # date to which the user is supposed to take the medicine
    takenTo = models.DateField(blank=True, null=True)

@receiver(pre_delete, sender=MedicineDosing, dispatch_uid='MedicineDosing_delete_signal')
def onDeleteMedicineDosing(sender, instance, using, **kwargs):
    """
    Remove all unnecessary adherence time objects.
    """
    for adherenceTime in instance.adherenceTimes:
        try:
            if not adherenceTime.isPredefined:
                adherenceTime.delete()
        except ProtectedError:
            pass 

class Treatment(models.Model):
    """
    Model of the treatment.
    """
    # reference to the caretaker
    caretaker = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    
    # predefined times
    predefinedTimes = models.ManyToManyField(AdherenceTime)
    
    # list of medicines in the treatment
    medicines = models.ManyToManyField(MedicineDosing)
    
    # max deviation without adherence score loss in minuts
    maxDeviation = models.IntegerField(blank=True, null=True)
    
    # patient first name
    patientFirstName = models.CharField(max_length=30)
    
    # patient second name
    patientLastName = models.CharField(max_length=150)
