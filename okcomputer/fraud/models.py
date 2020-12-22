from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)  #this class is an extension to the inbuilt User Model and this line says that the user object is Primary Key
    #additional objects besides the User model
    profile_pic = models.ImageField(blank= True , upload_to ='profile_pics')

    def __str__(self):
        return self.user.username

PAYMENT_METHODS = [('cashout', 'CASH OUT'), ('payment','PAYMENT'), ('cashin','CASH IN'), ('transfer','TRANSFER'), ('debit', 'DEBIT')]

class Transaction(models.Model):

    step = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    nameOrig = models.CharField(max_length=200)
    old_balance_org = models.FloatField(default=0)
    new_balance_org = models.FloatField(default=0)
    nameDest = models.CharField(max_length=200)
    old_balance_dest = models.FloatField(default=0)
    new_balance_dest = models.FloatField(default=0)
    transaction_type = models.CharField(max_length=200, default='cashout')
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    testing = models.CharField(max_length=200,default='null')
    

    def __str__(self):
        return str(self.amount)
    def get_absolute_url(self):
        return reverse('fraud:result')
    
