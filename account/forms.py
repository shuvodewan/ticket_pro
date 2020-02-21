#import user model
from django.contrib.auth import get_user_model
from .models import Profile

#import form
from django import forms 

user=get_user_model()


class UserCreationForm(forms.ModelForm):
    password=forms.CharField( max_length=50, required=True,widget=forms.PasswordInput(attrs={'type':"password" ,'class':"form-control" ,'placeholder':"password"}))
    confirm_password=forms.CharField(max_length=50, required=True,widget=forms.PasswordInput(attrs={'type':"password" ,'class':"form-control" ,'placeholder':"password"}))

    class Meta():
        model=user
        fields=['username','email']

        widgets={
            'username':forms.TextInput(attrs={'type':"text" ,'class':"form-control" ,'placeholder':"Username"}),
            'email'   :forms.EmailInput(attrs={'type':"email" ,'class':"form-control" ,'placeholder':"Email"})
            
        }

    def clean_confirm_password(self):
        password=self.cleaned_data["password"]
        confirm_password=self.cleaned_data['confirm_password']
        if password==confirm_password:
            if len(password)<8:
                raise forms.ValidationError("Password Mustbe 8 digite")
            else:
                return confirm_password
        else:
            raise forms.ValidationError('Both password fields Must be same') 

                       
class ProfileForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields=['firstname','lastname','image','phonenumber']            
            
        widgets={
            'firstname':forms.TextInput(attrs={'type':"text" ,'class':"form-control" ,'placeholder':"Firstname"}),
            'lastname':forms.TextInput(attrs={'type':"text" ,'class':"form-control" ,'placeholder':"Lastname"}),
            'phonenumber':forms.TextInput(attrs={'type':"text" ,'class':"form-control" ,'placeholder':"Phonenumber"}),
            'image':forms.FileInput(attrs={'class':"form-control"}),
            
            
        }    
class UserUpdateForm(forms.ModelForm):
   
    class Meta():
        model=user
        fields=['username','email','is_staff']

        widgets={
            'username':forms.TextInput(attrs={'type':"text" ,'class':"form-control" ,'placeholder':"Username"}),
            'email'   :forms.EmailInput(attrs={'type':"email" ,'class':"form-control" ,'placeholder':"Email"})
            
        }            