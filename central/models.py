from django.db import models


class Squirrel(models.Model):
    """In this class, 
    we set and define dataset attributes to create the Squirrel database.
    """
    loc_X = models.FloatField()
    loc_Y = models.FloatField()
    uniqueID = models.CharField(max_length=255)
    hectare = models.CharField(max_length=255)
    shift = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    hectareNum = models.IntegerField()
    age = models.CharField(max_length=255)
    primaryColor = models.CharField(max_length=255)
    highlightColor = models.CharField(max_length=255)
    combiColor = models.CharField(max_length=255)
    colorNotes = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    measurement = models.CharField(max_length=255)
    specificLocation = models.CharField(max_length=255)
    running = models.CharField(max_length=255)
    chasing = models.CharField(max_length=255)
    climbing = models.CharField(max_length=255)
    eating = models.CharField(max_length=255)
    foraging = models.CharField(max_length=255)
    otherActivities = models.CharField(max_length=255)
    kuks = models.CharField(max_length=255)
    quaas = models.CharField(max_length=255)
    moans = models.CharField(max_length=255)
    tailFlags = models.CharField(max_length=255)
    tailTwitches = models.CharField(max_length=255)
    approaches = models.CharField(max_length=255)
    indifferent = models.CharField(max_length=255)
    runsFrom = models.CharField(max_length=255)
    otherInteractions = models.CharField(max_length=255)
    latLong = models.CharField(max_length=255)
    zipcodes = models.CharField(max_length=255)
    communityDistricts = models.IntegerField()
    boroughBoundaries = models.IntegerField()
    cityCouncilDistricts = models.IntegerField()
    policePrecincts = models.IntegerField()

    class Meta:
        verbose_name_plural = "Squirrel"

    # def __str__(self):
    #     return self.uniqueID
