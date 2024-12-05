from django.shortcuts import render, redirect
from .forms import RegisterUser, LoginUser, UpdateEventForm,CreateEventForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateEventForm
from .models import CreateEvent
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def home(request):
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
            return redirect('home')
        
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



def event_list(request):
    events = CreateEvent.objects.all()
    total_events_count = CreateEvent.objects.count()
    total_users = User.objects.count()
    
    return render(request, 'core/event_list.html', {'total_events':total_events_count,
                                                    'events': events,
                                                    'total_users': total_users})

def event_view_admin(request,pk):
    events = CreateEvent.objects.get(id = pk)
    context = {'events':events}
    return render(request,"core/event_view_admin.html",context=context)

def event_book(request, pk):

    events = get_object_or_404(CreateEvent, id=pk)
    context = {'events': events}
    return render(request, "core/event_book.html", context)

# def total_events(request):
#     total_events_count =  CreateEvent.objects.count()
#     context = {'total_events': total_events_count}
#     return (context)

