import json
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from .forms import RegisterUser, LoginUser, UpdateEventForm,CreateEventForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import uuid
from django.views import View
from  django.http import HttpResponseRedirect, JsonResponse
from django.utils.timezone import now

def home(request):
    request.is_approved = approve_user(request )
    return render(request, 'core/index.html')

# def event_page(request):
#     return render(request, 'core/events.html')

def user_register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home',{'user':user})
        
    else:
        form = RegisterUser()
    return render(request,'core/register.html',{'form':form})

def user_login(request):

    if request.method == 'POST':
        form = LoginUser(request,request.POST)
        if form.is_valid():
            print("logged in a")
            # Retrieve credentials from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                print("logged in")
                return redirect('home')
            else:
                # Add an error message if authentication fails
                form.add_error(None, 'Invalid username or password')
        else:
   
            print('a',form)

    else:
        # Initialize the form for GET requests
        form = LoginUser()

    return render(request, 'core/login.html', {'form': form})

    

def user_logout(request):
    logout(request)
    messages.success(request,"Logout success!")
    return redirect('home')


@login_required(login_url = "user_login")
def create_event(request):
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, "Your event was created")
            return redirect('home')
    else:
        # Initialize the form for GET request
        form = CreateEventForm()

    event_categories = CreateEvent.EVENT_CATEGORY
    return render(request, 'core/create_event.html', {'form': form,
                                                      'event_categories': event_categories})





@login_required(login_url = "user_login")
def trade_event(request, pk):
    events  = CreateEvent.objects.get(id= pk)
    return render(request,'core/trade_event.html', {'events': events})


# @login_required(login_url = "user_login")
# def trade_event_buyer(request):
#     return render(request, "core/trade_event_buyer.html")

# @login_required(login_url = "user_login")
# def trade_event_seller(request):
#     return render(request, "core/trade_event_seller.html")




@login_required(login_url = "user_login")
def update_event(request, pk):

    events = CreateEvent.objects.get(id=pk)
    event_categories = CreateEvent.EVENT_CATEGORY
    
    print(events)
    # form = UpdateEventForm(instance=events)

    if request.method == 'POST':
        form = UpdateEventForm(request.POST, instance=events) 
        if form.is_valid():
            form.save()
            messages.success(request, "Your event was updated")
            return redirect(event_list)
        
    return render(request,"core/update_event.html",{'events':events,
                                                    'pk':pk,
                                                    'event_categories': event_categories})
    

def event_page(request):
    events = CreateEvent.objects.all()
    
    return render(request, 'core/events.html',{'events':events})


@login_required(login_url= "user_login")
def delete_event(request,pk):
    events = CreateEvent.objects.get(id=pk)
    events.delete()
    messages.success(request,"Your event was deleted")
    return redirect('event_list')




def user_list(request):
    users = User.objects.all()
    total_users = User.objects.count()
    total_events_count = CreateEvent.objects.count()
    total_orgs = Be_an_organizer.objects.count()

    return render(request, 'core/users.html', {'users':users,
                                               'total_users': total_users,
                                               'total_events':total_events_count,
                                               'total_orgs':total_orgs})

def org_list(request):
    orgs = Be_an_organizer.objects.all()
    total_users = User.objects.count()
    total_events_count = CreateEvent.objects.count()
    total_orgs = Be_an_organizer.objects.count()

    return render(request, 'core/org.html',{'orgs':orgs,
                                            'total_users': total_users,
                                            'total_events': total_events_count,
                                            'total_orgs': total_orgs
                                            })



def event_list(request):
    events = CreateEvent.objects.all()
    total_events_count = CreateEvent.objects.count()
    total_users = User.objects.count()
    total_orgs = Be_an_organizer.objects.count()
    
    return render(request, 'core/event_list.html', {'total_events':total_events_count,
                                                    'events': events,
                                                    'total_users': total_users,
                                                    'total_orgs': total_orgs})

def event_view_admin(request,pk):
    events = CreateEvent.objects.get(id = pk)
    context = {'events':events}
    return render(request,"core/event_view_admin.html",context=context)

def event_book(request, pk):
    events = get_object_or_404(CreateEvent, id=pk)
    context = {'events': events}
    return render(request, "core/event_book.html", context)

def trade_event_seller(request):
    if request.method == "POST":
        name = request.POST.get("name")
        company_name = request.POST.get("company_name")
        location = request.POST.get("location")
        services = request.POST.get("services")

        print(f"Received data: name={name}, company_name={company_name}, location={location}, services={services}")

        if not name or not company_name or not location or not services:
            messages.error(request, "All fields are required.")
            return render(request, 'core/trade_event_seller.html')
        
        existing_seller = Seller.objects.filter(company_name=company_name).first()
        if existing_seller:
            messages.warning(request, "You are already registered as a seller!")
            return render(request, 'core/trade_event_seller.html')

        try:
            # Attempt to create a Seller object
            seller = Seller.objects.create(
                name=name,
                company_name=company_name,
                location=location,
                services=services
            )
            print(f"Seller saved: {seller}")
            messages.success(request, "Successfully registered as a Seller!")
            return render('core/trade_event.html')  # Replace with your correct URL name
        except Exception as e:
            print(f"Error while saving seller: {e}")
            messages.error(request, f"An error occurred: {e}")
            return render(request, 'core/trade_event_seller.html')

    return render(request, 'core/trade_event_seller.html')




# def schedule_meetings(request):
#     if request.method == 'POST':
#         selected_sellers_ids = request.POST.getlist('sellers')  # Retrieve selected seller IDs from the form
#         print("Selected Seller IDs:", selected_sellers_ids)  # Debug: print the IDs
#         selected_sellers = Seller.objects.filter(id__in=selected_sellers_ids)  # Filter sellers by IDs
#         print("Selected Sellers:", selected_sellers)  # Debug: print the queryset
#         return render(request, 'core/success.html', {'selected_sellers': selected_sellers})  # Pass to template
#     return HttpResponseRedirect(reverse('select-seller'))



@login_required(login_url="user_login")
def be_an_org(request):
    if request.method == "POST":
        organization_name = request.POST.get('organization_name')
        organizer_name = request.POST.get('organizer_name', '')
        organization_address = request.POST.get('organization_address', '')
        organization_email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        website = request.POST.get('website', '')

        if not organization_name or not organization_email:
            messages.error(request, "Organization name and email are required.")
            return render(request, 'core/be_an_org.html')  # Re-render with error message

        # Create the Be_an_organizer instance
        Be_an_organizer.objects.create(
            organization_name=organization_name,
            organizer_name=organizer_name,
            organization_address=organization_address,
            organization_email=organization_email,
            phone_number=phone_number,
            website=website,
            user = request.user,
            is_approved = False
        )
        messages.success(request, "Successfully registered as an organizer.")
        return redirect('home')

    return render(request, 'core/be_an_org.html')   


def approve_user(request):
    if not request.user.is_authenticated:
        return False  # Anonymous users are not approved

    try:
        organizer = Be_an_organizer.objects.get(user=request.user)
        return organizer.is_approved
    except Be_an_organizer.DoesNotExist:
        return False

@login_required(login_url="user_login")
def booking(request):
    return render(request,"core/booking.html")




@login_required(login_url = "user_login")
def buy_ticket(request, event_id):
    event = get_object_or_404(CreateEvent, id = event_id )
   
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity',0))
        if event.total_ticket >= quantity and quantity > 0:
            event.total_ticket -= quantity
            event.save()

            total_amount = quantity * event.price

            Ticket.objects.create(event = event, buyer=request.user, quantity=quantity)
            return redirect ('khalti-payment', total_amount = total_amount)

        return render(request, 'core/event_book.html',{
            'event': event,
            'error': 'not enough tickets'
        })

    return render(request, 'events.html', {'event':event})


def select_sellers_view(request):
    if request.method == 'POST':
        selected_sellers_ids = request.POST.getlist('sellers')
        buyer = request.user

        selected_sellers = Seller.objects.filter(id__in=selected_sellers_ids)

        for seller in selected_sellers:
            Meeting.objects.create(buyer = buyer,
                                   seller = seller,
                                   scheduled_date = now().date(),
                                   scheduled_time = now().time())


        return render(request, 'core/success.html', {'selected_sellers': selected_sellers})
    
    sellers  = Seller.objects.all()
    return render (request, 'core/trade_event_buyer.html',{'sellers': sellers})




@login_required(login_url="user_login")
def my_tickets(request):
    tickets = Ticket.objects.filter(buyer = request.user)
    return render(request, 'core/my_tickets.html',{'tickets':tickets})

def khalti_payment(request, total_amount):
    return render(request, "core/khalti.html",{'total_amount':total_amount})



# class KhaltiRequestView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}  # Corrected the syntax error
#         return render(request, "core/khaltirequest.html", context)
    

# class KhaltiVerifyView(View):
#     def get(self, request, *args, **kwargs):
#         data = {}

#         return JsonResponse(data)


@login_required(login_url="user_login")
def khaltihome(request, event_id):
    event = CreateEvent.objects.get(id = event_id)
    id = uuid.uuid4()
    print(id)
    return render(request, 'core/khaltirequest.html', {'uuid':id,
                                                       'event':event})


@login_required(login_url="user_login")
def initKhalti(request, event_id, total_amount      ):
    url = "https://a.khalti.com/api/v2/epayment/initiate/"
    return_url = request.POST.get('return_url')
    website_url = request.POST.get('return_url')
    amount = request.POST.get('amount')
    purchase_order_id = request.POST.get('purchase_order_id')

    user = request.user
    event = CreateEvent.objects.get(id = event_id)

    print(f"User: {user.username}")
    print(f"Event: {event.event_title}")
    print(f"Amount: {event.price}")



    print(user)
    print("url",url)
    print("return_url",return_url)
    print("web_url",website_url)
    print("amount",total_amount)
    print("purchase_order_id",purchase_order_id)


    payload = json.dumps({
        "return_url": return_url,
        "website_url": website_url,
        "amount": event.price,
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": event.event_title,
        "customer_info": {
        "name": user.username,
        "email": user.email,
        "phone": "9800000001"
        }
    })

    # put your own live secet for admin
    headers = {
        'Authorization': 'key d1f3a5b6b40644efbb4d7519c4eba762',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(json.loads(response.text))

    print(response.text)
    new_res = json.loads(response.text)
    # print(new_res['payment_url'])
    print(type(new_res))
    return redirect(new_res['payment_url'])
    return redirect("home")

@login_required(login_url="user_login")
def verifyKhalti(request):
    url = "https://a.khalti.com/api/v2/epayment/lookup/"
    if request.method == 'GET':
        headers = {
            'Authorization': 'key d1f3a5b6b40644efbb4d7519c4eba762',
            'Content-Type': 'application/json',
        }
        pidx = request.GET.get('pidx')
        data = json.dumps({
            'pidx':pidx
        })
        res = requests.request('POST',url,headers=headers,data=data)
        print(res)
        print(res.text)

        new_res = json.loads(res.text)
        print(new_res)
        

        if new_res['status'] == 'Completed':
            # user = request.user
            # user.has_verified_dairy = True
            # user.save()
            # perform your db interaction logic
            pass
        
        # else:
        #     # give user a proper error message
        #     raise BadRequest("sorry ")

        return redirect('home')
