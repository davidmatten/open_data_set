from django.db import models

# Create your models here.


import os

class dataset(models.Model):
    name = models.CharField(db_column = "name", max_length = 100)
    description = models.CharField(db_column = "description", max_length = 1000)
    is_public = models.BooleanField(db_column = "is_public", default=False)
    area_covered = models.CharField(db_column = "area_covered", max_length = 765)
    participants = models.IntegerField(db_column = "participants")
    is_longitudinal = models.BooleanField(default=False)
    contact_details = models.CharField(max_length = 1000)
    fields_collected = models.TextField()
#    study_docs = models.FileField( http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example
    Abstract = models.CharField(max_length = 1000)
