from django.db import models

# Create your models here.
class coding_event_query(models.Model):
    keyword = models.CharField(max_length=160)
    date = models.DateField()
    location = models.CharField(max_length=160)


