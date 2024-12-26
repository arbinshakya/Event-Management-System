from django.urls import path, include
from . import views
from django.views import View
# from .views import KhaltiRequestView, KhaltiVerifyView

urlpatterns = [

    path('',views.home, name = 'home'),
    path('booking',views.booking, name = 'booking'),
    path('profile',views.profile, name = 'profile'),



    path('register/',views.user_register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('user-logout/', views.user_logout, name = "user-logout"),
    path('create-event/', views.create_event, name = "create-event"),
    # path('event-page/', views.event_page, name = "event-page"),

    # path('get-tickets/',views.get_tickets, name = 'get-tickets'),

    #khalti
    path('khalti-home/',views.khaltihome, name = "khalti-home"),
    path('initiate/', views.initKhalti, name = "initiate" ),
    path('verify/', views.verifyKhalti, name = "verify" ),


    # path('khalti-request/', KhaltiRequestView.as_view(), name="khalti-request"),
    # path('khalti-verify/', KhaltiVerifyView.as_view(), name = "khalti-verify"),

    path('event-page/', views.event_page, name = "event-page"),
    path('trade-event/<int:pk>', views.trade_event, name = "trade-event"),
    # path('trade-event_buyer/', views.trade_event_buyer, name = "trade-event-buyer"),
    path('trade-event_seller/', views.trade_event_seller, name = "trade-event-seller"),
    path('select-seller/', views.select_sellers_view, name = "select-seller"),
    # path('select-meeting', views.schedule_meetings, name = "select-meeting"),
    path('buyer-registration/', views.buyers, name = "buyer-registration"),
    path('buyer-profile/', views.buyer_profile, name = "buyer-profile"),
    path('manage-meetings/', views.manage_meetings, name= 'manage-meetings'),
    path('seller-buyers/', views.seller_buyer_views, name= 'seller-buyers'),



    path('my-tickets/', views.my_tickets, name = "my_tickets"),
    # path('total-price/<int:event_id>/',views.total_price, name = "total-price"),
    path('update-event/<int:pk>/', views.update_event, name = "update-event"),
    path('event-list/', views.event_list, name = "event-list"),
    path('user-list/', views.user_list, name = "user-list"),
    path('org-list/',views.org_list, name = "org-list"),
    path('buy-ticket/<int:event_id>/', views.buy_ticket, name = "buy_ticket"),
    path('khalti-payment/<int:total_amount>/', views.khalti_payment, name = "khalti-payment"),

    # path('event-list/', views.total_events, name = "event-list"),

    # path('initiate', views.initkhalti, name = "initiate"),
    # path( ' verify', views.verifykhalti, name = "verify"),





    path('event-view-admin/<int:pk>/', views.event_view_admin, name = "event-view-admin"),
    path('delete-event/<int:pk>/',views.delete_event,name = "delete-event"),
    path('event-book/<int:pk>/',views.event_book,name = "event-book"),

    path('be-an-org/', views.be_an_org, name="be-an-org"),


]
