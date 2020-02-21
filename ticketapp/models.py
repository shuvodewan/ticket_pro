from django.db import models
from django.contrib.auth import get_user_model

user=get_user_model()

# Create your models here.

class Complain(models.Model):
    subject=models.CharField(max_length=100,null=True,blank=True)
    complain=models.CharField(max_length=500,null=True,blank=True)
    image= models.ImageField(upload_to="complain_image",default='default.png')
    user=models.ForeignKey(user,on_delete=models.CASCADE ,null=True)
    date=models.DateField(auto_now=True)
    raised=models.BooleanField(default=False)
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.subject

class Ticket(models.Model):
    complain=models.OneToOneField(Complain, on_delete=models.CASCADE)
    details=models.CharField(max_length=500,null=True,blank=True)  
    date=models.DateTimeField(auto_now=True)
    concern=models.ForeignKey(user,on_delete=models.DO_NOTHING) 
    ticket_id=models.CharField(max_length=100 ,null=True,blank=True)  
    status=models.CharField(max_length=50,choices=[('Processing','Processing'),('Solved','Solved'),('Closed','Closed')],default="Raised")



    def __str__(self):
        return self.ticket_id   

class Conversation(models.Model):
    text=models.CharField(max_length=500,null=True,blank=True)
    ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user=models.ForeignKey(user,on_delete=models.DO_NOTHING,null=True)
    date=models.DateTimeField(auto_now=True)
      

    def  __str__(self):
        return self.ticket.ticket_id    

class Log(models.Model):
    message=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.message