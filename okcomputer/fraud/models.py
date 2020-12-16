from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)  #this class is an extension to the inbuilt User Model and this line says that the user object is Primary Key

    #additional objects besides the User model

    

    profile_pic = models.ImageField(blank= True , upload_to ='profile_pics')

    def __str__(self):
        return self.user.username

PAYMENT_METHODS = [('cashout', 'CASH OUT'), ('payment','PAYMENT'), ('cashin','CASH IN'), ('transfer','TRANSFER'), ('debit', 'DEBIT')]

class Transaction(models.Model):

    amount = models.IntegerField()
    old_balance_org = models.IntegerField()
    new_balance_org = models.IntegerField()
    old_balance_dest = models.IntegerField()
    new_balance_dest = models.IntegerField()
    cat = models.IntegerField(choices=PAYMENT_METHODS,default='cashout')

    def __str__(self):
        return self.amount

