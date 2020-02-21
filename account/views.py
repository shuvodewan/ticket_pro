from django.shortcuts import render,get_object_or_404
from .forms import UserCreationForm,ProfileForm,UserUpdateForm
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Profile as UserProfile
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required

Member=get_user_model()

# Create your views here.

@staff_member_required(login_url="login")
def UserCreate(request):
    form=UserCreationForm()
    profileform=ProfileForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        profileform=ProfileForm(request.POST,request.FILES)
        if form.is_valid() and profileform.is_valid():
            user=form.save(commit=False)
            profile=profileform.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile.user=user
            profile.save()
            return render(request,'index.html')


    return render(request,'add_user.html',{'form':form,'profileform':profileform})

@staff_member_required(login_url="login")
def list_user(request):
    search_result_p=[]
    if request.method=="POST":   
        search=request.POST.get("search")
        if len(search)!=0:
            search_result_p=Member.objects.filter(Q(username__contains=search)|Q(username__contains=search))  
            print(search_result_p)                                                                                               
            if len(search_result_p)==0:
                messages.error(request,'No match found')
    users=Member.objects.filter(is_staff=False)
        # users pagignator
    paginator_p = Paginator(users, 2) # Show 25 contacts per page
    users_p = request.GET.get('users')
    users_p_p = paginator_p.get_page(users_p) 
                                                  
    context={
        'users':users_p_p,
        'search':search_result_p
    }
    return render(request,'user_list.html',context)  
@staff_member_required(login_url="login")
def update_user(request,pk):
    instance=get_object_or_404(Member,pk=pk)
    instance_profile=UserProfile.objects.filter(user=instance)
    form=UserUpdateForm(instance=instance)
    for instance_profile in instance_profile:
        instance_profile=instance_profile
    profileform=ProfileForm(instance=instance_profile)
    if request.method=="POST":
        form=UserUpdateForm(request.POST,instance=instance)
        profileform=ProfileForm(request.POST,request.FILES,instance=instance_profile)
        if form.is_valid() and profileform.is_valid():
            user=form.save(commit=False)
            profile=profileform.save(commit=False)
            if request.POST['password'] and request.POST['confirm_password']:
                if request.POST["password"]==request.POST["confirm_password"]:
                    if len(request.POST['password'])>8:
                        user.set_password(request.POST['confirm_password'])    
            user.save()
            profile.save()
            messages.success(request,'update successfully')
        else:
            messages.error(request,'not Valid')       
    context={
        'form':form,
        'profileform':profileform,
        'instance':instance
    }
    return render(request,'update_user.html',context)

@staff_member_required(login_url="login")  
def delete_user(request,pk):
    Member.objects.filter(pk=pk).delete()
    messages.success(request,'Delete successfull')
    return HttpResponseRedirect(reverse('account:user_list'))

@staff_member_required(login_url="login")
def member_list(request):
    search_result_p=[]
    if request.method=="POST":   
        search=request.POST.get("search")
        if len(search)!=0:
            search_result_p=Member.objects.filter(Q(username__contains=search)|Q(username__contains=search))  
            print(search_result_p)                                                                                               
            if len(search_result_p)==0:
                messages.error(request,'No match found')
    users=Member.objects.filter(is_staff=True,is_superuser=False)
        # users pagignator
    paginator_p = Paginator(users, 2) # Show 25 contacts per page
    users_p = request.GET.get('users')
    users_p_p = paginator_p.get_page(users_p) 
                                                  
    context={
        'users':users_p_p,
        'search':search_result_p
    }
    return render(request,'user_list.html',context)  

