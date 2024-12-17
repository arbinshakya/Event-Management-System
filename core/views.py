from django.shortcuts import render, redirect
from .forms import RegisterUser, LoginUser, UpdateEventForm,CreateEventForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


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
    return render(request, 'core/create_event.html', {'form': form})


@login_required(login_url = "user_login")
def update_event(request, pk):

    events = CreateEvent.objects.get(id=pk)
    
    print(events)
    # form = UpdateEventForm(instance=events)

    if request.method == 'POST':
        form = UpdateEventForm(request.POST, instance=events) 
        if form.is_valid():
            form.save()
            messages.success(request, "Your event was updated")
            return redirect(event_list)
        
    return render(request,"core/update_event.html",{'events':events,
                                                    'pk':pk})
    

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

            Ticket.objects.create(event = event, buyer=request.user, quantity=quantity)
            return redirect (event_page)

        return render(request, 'core/event_book.html',{
            'event': event,
            'error': 'not enough tickets'
        })

    return render(request, 'events.html', {'event':event})


@login_required(login_url="user_login")
def my_tickets(request):
    tickets = Ticket.objects.filter(buyer = request.user)
    return render(request, 'core/my_tickets.html',{'tickets':tickets})

