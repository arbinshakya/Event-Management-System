from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.home, name = 'home'),
    path('register/',views.user_register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('user-logout/', views.user_logout, name = "user-logout"),
    path('create-event/', views.create_event, name = "create-event"),
    # path('event-page/', views.event_page, name = "event-page"),

    path('event-page/', views.event_page, name = "event-page"),
    path('update-event/<int:pk>/', views.update_event, name = "update-event"),
    path('event-list/', views.event_list, name = "event-list"),
    # path('event-list/', views.total_events, name = "event-list"),

    path('event-view-admin/<int:pk>/', views.event_view_admin, name = "event-view-admin"),
    path('delete-event/<int:pk>/',views.delete_event,name = "delete-event"),
    path('event-book/<int:pk>/',views.event_book,name = "event-book"),

    path('be-an-org/', views.be_an_org, name="be-an-org"),


]
