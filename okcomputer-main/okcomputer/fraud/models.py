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
    amount = models.FloatField()
    old_balance_org = models.FloatField()
    new_balance_org = models.FloatField()
    old_balance_dest = models.FloatField()
    new_balance_dest = models.FloatField()
    transfer_type = models.CharField(max_length = 20,choices=PAYMENT_METHODS,default='cashout')
    cat = models.IntegerField(default=0)


    testing = models.CharField(max_length=200,default='null')

    def __str__(self):
        return str(self.amount)
    def get_absolute_url(self):
        return reverse('fraud:result')
    def first(self):
        objects = list()
        if objects:
            return objects[0]
        return None
