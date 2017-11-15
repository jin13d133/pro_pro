from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

class Hash(models.Model):
    hash_name = models.CharField(max_length=100, unique= True)
    hash_value= models.CharField(max_length=2000, unique=True)
    hash_type = models.CharField(max_length=10)
    hash_date = models.DateTimeField(default=datetime.now)

    def __str__(self):  # __unicode__ on Python 2
        return self.hash_name

class Virus_hash(models.Model):
    virus_file_name = models.CharField(max_length=100, unique=True)
    virus_hash_value = models.CharField(max_length=2000, unique= True)
    virus_detail = models.CharField(max_length=3000)
    virus_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.virus_file_name
