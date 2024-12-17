from datetime import date
from django.db import models
from django.contrib.auth.models import User

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
    price = models.IntegerField(default = 0)
    total_ticket = models.IntegerField(default=0)

    
    def __str__(self):
        return self.event_title
    

class Ticket(models.Model):
    event = models.ForeignKey(CreateEvent, on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default = 0)
    total_price = models.IntegerField(default = 0)

    def __str__(self):
        return self.event.event_title
    
    # def save(self, ):
    #     quantity = int(request.POST.get('quantity',1))
    #     if event.total_ticket >= quantity:
    #         event.total_ticket -= quantity
    #         event.save()
    


class Be_an_organizer(models.Model):
   
    organization_name = models.CharField(max_length=255)
    organizer_name = models.CharField(max_length=255)
    organization_address = models.CharField(max_length=255, null=True)
    organization_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank = True, null = True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default  = 1) 
    is_approved = models.BooleanField(default = False)

    def __str__(self):
        return self.organization_name
