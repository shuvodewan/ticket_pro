from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ComplainForm
from django.contrib import messages
from .models import Log,Complain,Ticket,Conversation
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
import random
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.db.models import Q
User=get_user_model()


# Create your views here.
@login_required
def index(request):
    if not request.user.is_staff:
        complain_form=ComplainForm()
        complain=Complain.objects.filter(raised=True,user=request.user)
        for complain in complain:
            complain=complain  
        context={
            'complain_form':complain_form,
            'complain':complain
        }
    else:    
        complain=Complain.objects.filter(status=False)
        complain_solved=Complain.objects.filter(status=True).count()
        total_client=User.objects.filter(is_staff=False).count()
        total_member=User.objects.filter(is_staff=True).count()
        # users pagignator
        paginator_c = Paginator(complain, 2) # Show 25 contacts per page
        complain_c = request.GET.get('complain')
        complain_c_c = paginator_c.get_page(complain_c) 
        context={
            'total_member':total_member,
            'total_client':total_client,
            'total_complain':len(complain),
            'total_solved':complain_solved,
            'complain':complain_c_c
        }
    return render(request,'index.html',context)
@login_required    
def createcomplain(request):
    if request.method=="POST":
        complain_form=ComplainForm(request.POST,request.FILES)
        if complain_form.is_valid():
            complain=complain_form.save(commit=False)
            complain.user=request.user
            complain.save()
            messages.success(request,'Wait our concern will takecare the issue soon')
            Log.objects.create(message="{} posted a complain".format(request.user),user=request.user)
            return HttpResponseRedirect(reverse("index"))

@staff_member_required(login_url="login")
def raisedticket(request,pk=None):

    complain=get_object_or_404(Complain,pk=pk)
    ticket=Ticket.objects.create(complain=complain,details=complain.complain,concern=request.user,ticket_id="T{}".format(random.randint(1000,50000)))
    complain.raised=True
    complain.save()
    Log.objects.create(message="{} A complain ticket has raised".format(complain.user),user=complain.user)
    messages.success(request,'A complete Ticket has raised')
    return HttpResponseRedirect(reverse('index'))

@login_required
def disc_ticket(request,pk):
    ticket=get_object_or_404(Ticket,pk=pk)
    context={
        'ticket':ticket
    }
    return render(request,'ticket.html',context)
@login_required
def conversation(request):
    if request.method=="POST":
        pk=request.POST['ticket']
        text=request.POST['message']
        ticket=get_object_or_404(Ticket,pk=pk)
        Conversation.objects.create(text=text,ticket=ticket,user=request.user)
        if request.user==ticket.concern:
            return HttpResponseRedirect(reverse('ticketapp:ticket_disc' ,kwargs={'pk': ticket.pk}))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))

@staff_member_required(login_url="login")        
def closeticket(request,pk):
    ticket=get_object_or_404(Ticket,pk=pk)
    ticket.status="solved"
    ticket.complain.raised=False
    ticket.complain.status=True
    ticket.complain.save()
    ticket.save()
    messages.success(request,'Ticket Has closed')
    return HttpResponseRedirect(reverse('index'))



@login_required
def list_Ticket(request):
    search_result_p=[]
    if request.method=="POST":   
        search=request.POST.get("search")
        if len(search)!=0:
            if request.user.is_staff:
                search_result_p=Ticket.objects.filter(Q(Ticket_id__contains=search)|Q(complain__username__contains=search))
            else:
                search_result_p=Ticket.objects.filter(ticket_id=search,complain__user=request.user)                                                                                                  
            if len(search_result_p)==0:
                messages.error(request,'No match found')
    ticket=Ticket.objects.filter(status="solved")
    ticket_user=Ticket.objects.filter(status="solved",complain__user=request.user)
        # ticket pagignator
    paginator_t = Paginator(ticket, 5) # Show 25 contacts per page
    ticket_t = request.GET.get('ticket')
    ticket_t_t = paginator_t.get_page(ticket_t) 

        # ticket pagignator
    paginator_u = Paginator(ticket_user, 5) # Show 25 contacts per page
    ticket_u = request.GET.get('ticket')
    ticket_u_u = paginator_u.get_page(ticket_u)
    if request.user.is_staff:                                               
        context={
            'ticket':ticket_t_t,
            'search':search_result_p
        }
    else:
         context={
            'ticket':ticket_u_u,
            'search':search_result_p
        }    
    return render(request,'ticket_list.html',context)  

    
