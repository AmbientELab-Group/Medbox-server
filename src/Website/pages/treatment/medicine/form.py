"""
Form for adding medicine.
"""

__author__ = "Krzysztof Adamkiewicz"
__status__ = "development"
__date__ = "23.5.2020"

from django import forms

class MedicineForm(forms.Form):
    """
    Medicine form.
    """
    # name of the medicine
    name = forms.CharField(max_length=500)
    
    # is medicine only taken in case of emergencies?
    emergency = forms.BooleanField(required=False, initial=False)
    
    # dose of the medicine
    dose = forms.IntegerField(initial=1)
    
    # time of taking the medicine
    timeOfTaking = forms.TimeField(widget=forms.TimeInput)
    
    # dates of medicine taking
    takenTo = forms.DateField(widget=forms.SelectDateWidget)
    takenFrom = forms.DateField(required=False, widget=forms.SelectDateWidget) 
