from datetime import date
from django.db import models
from django.contrib.auth.models import User

class CreateEvent(models.Model):

    CONCERT = 'Concert'
    TRADE = 'Trade'

    EVENT_CATEGORY =[
        (CONCERT, 'Concert'),
        (TRADE, 'Trade')
    ]

    event_title = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=255)
    event_category = models.CharField(max_length=255, choices=EVENT_CATEGORY, default=CONCERT)
    city = models.CharField(max_length=255)
    post_code = models.IntegerField()
    province = models.CharField(max_length=255)
    event_date = models.DateField(default=date.today)  # Set the default to today's date
    event_time = models.TimeField()
    description = models.TextField()
    event_organizer = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    price = models.IntegerField(default = 0, blank= True)
    total_ticket = models.IntegerField(default=0, blank= True)

    
    def __str__(self):
        return self.event_title


METHOD = (
    # ("Door sale","Door sale"),
    ("Khalti","Khalti"),
)


class Ticket(models.Model):
    event = models.ForeignKey(CreateEvent, on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default = 0)
    total_price = models.IntegerField(default = 0)
    payment_method = models.CharField(max_length = 20, choices = METHOD)
    payment_completed = models.BooleanField(default = False, null = True, blank= True)

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
        return f"{self.organization_name}"



class TradeEvent(models.Model):
    company_name = models.CharField(max_length = 255)
    company_email = models.CharField(max_length =255)

    def __str__(self):
        return self.company_name
    

class Buyer(models.Model):
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255, null= True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='buyers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Seller(models.Model):
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length = 255)
    location = models.CharField(max_length=100)
    services = models.TextField()
    email = models.EmailField(default='example@example.com')
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='sellers')
    

    def __str__(self):
        return self.company_name
    
    
class Meeting(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()


    def __str__(self):
        return f"{self.seller.company_name}" 


