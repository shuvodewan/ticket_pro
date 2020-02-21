from django.contrib import admin

from .models import Complain,Ticket,Conversation,Log


# Register your models here.
admin.site.register(Complain)
admin.site.register(Ticket)
admin.site.register(Conversation)
admin.site.register(Log)