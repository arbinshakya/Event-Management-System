from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.home, name = 'home'),
    path('booking',views.booking, name = 'booking'),

    path('register/',views.user_register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('user-logout/', views.user_logout, name = "user-logout"),
    path('create-event/', views.create_event, name = "create-event"),
    # path('event-page/', views.event_page, name = "event-page"),

    # path('get-tickets/',views.get_tickets, name = 'get-tickets'),

    path('event-page/', views.event_page, name = "event-page"),
    path('my-tickets/', views.my_tickets, name = "my_tickets"),
    # path('total-price/<int:event_id>/',views.total_price, name = "total-price"),
    path('update-event/<int:pk>/', views.update_event, name = "update-event"),
    path('event-list/', views.event_list, name = "event-list"),
    path('user-list/', views.user_list, name = "user-list"),
    path('org-list/',views.org_list, name = "org-list"),
    path('buy-ticket/<int:event_id>/', views.buy_ticket, name = "buy_ticket"),


    # path('event-list/', views.total_events, name = "event-list"),




    path('event-view-admin/<int:pk>/', views.event_view_admin, name = "event-view-admin"),
    path('delete-event/<int:pk>/',views.delete_event,name = "delete-event"),
    path('event-book/<int:pk>/',views.event_book,name = "event-book"),

    path('be-an-org/', views.be_an_org, name="be-an-org"),


]
