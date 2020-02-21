from django.db import models

#import usermodel

from django.contrib.auth import get_user_model

member=get_user_model()

# Create your models here.

class Profile(models.Model):

    image=models.ImageField(upload_to="profile_pic", null=True,blank=True)
    firstname=models.CharField(max_length=50,blank=True,null=True)
    lastname=models.CharField(max_length=50,blank=True,null=True)
    phonenumber=models.CharField(max_length=11,blank=True,null=True)
    user=models.OneToOneField(member, on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)


    def __str__(self):
        return self.user.username