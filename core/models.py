from datetime import date
from django.db import models

class CreateEvent(models.Model):
    event_title = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    post_code = models.IntegerField()
    province = models.CharField(max_length=255)
    event_date = models.DateField(default=date.today)  # Set the default to today's date
    event_time = models.TimeField()
    description = models.TextField()
    event_organizer = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.event_title
