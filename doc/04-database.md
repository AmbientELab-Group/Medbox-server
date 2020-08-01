# Model list

Database  is handled entirely by django.

Generally one model = one table.

Here are all the models in the database:


## Models related to the device

#### Device model

One record per device. It contains a serial number, a human readable name and a list of users to which the device is assigned.

```
class Device(models.Model):
    """
    Model of the device.
    """
    # unique serial number of the device
    serialNumber = models.UUIDField(primary_key=True, editable=False)
    
    # name given to the device by user
    name = models.CharField(max_length=100, blank=True, null=True)
    
    # users to which the device is assigned
    users = models.ManyToManyField(get_user_model())
```

#### Device authentication token

Random token assigned to each device. It is send with each API request and identifies the device.

```
class DeviceApiToken(models.Model):
    """
    Model of the device token for API.
    """
    # key itself
    token = models.CharField(max_length=42)
    
    # device to which the token is assigned
    device = models.OneToOneField(Device, on_delete=models.PROTECT)

```

#### Device pairing key

6-digit code used for pairing.

```
class DevicePairingKey(models.Model):
    """
    Model of the key used for paring of the device.
    """
    # key itself
    key = models.CharField(max_length=6)
    
    # device to which the key is assigned
    device = models.OneToOneField(Device, on_delete=models.PROTECT)
    
    # expiration time
    expires = models.DateTimeField()

```

## Models related to treatment

#### Medicine

Contains all properties of a medicine.

```
class Medicine(models.Model):
    """
    Model of the medicine.
    """
    # name of the medicine
    name = models.CharField(max_length=500) 
```

#### Adherence Time

This model contains a time at which a medicine is taken.
This way user can predefine a number of times. This might be an overcomplication.

```
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
```

#### Medicine Dosing

It contains an information about at what times is the medicine taken.
I think this is quite an overcomplication.

```
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
```

#### Treatment model

This model contains a treatment profile (list of medicines and times at which they are taken).

```
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
```
