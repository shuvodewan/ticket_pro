from django.urls import path,include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name="ticketapp"

urlpatterns=[
    path('complain_create',views.createcomplain,name='complain_create'),
    path('raise_ticket/<int:pk>',views.raisedticket,name="raise_ticket"),
    path('ticket_disc/<int:pk>',views.disc_ticket,name='ticket_disc'),
    path('conversation',views.conversation,name="conversation"),
    path('close_ticket/<int:pk>',views.closeticket,name='closeticket'),
    path('ticket_list',views.list_Ticket,name='ticket_list'),
]
