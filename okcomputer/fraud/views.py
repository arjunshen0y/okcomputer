from django.shortcuts import render
from . import forms
from .forms import UserForm,UserExtra,Transaction_Details

#Imports needed for Login

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request, 'fraud/index.html')

def register(request):
    
    registered = False                  # first we assume that the user has not registered

    if request.method == 'POST':
        user_form = UserForm(request.POST)  #   # these two variables are instances of the model forms while request is post
        profile_form = UserExtra(request.POST)

        if user_form.is_valid() and profile_form.is_valid():        #checks wheather the two forms are valid

            user = user_form.save()             #saves the data from the form
            user.set_password(user.password)    #sets the password , also hashing is undergone
            user.save()                         #saves data and pswd

            profile = profile_form.save(commit=False)  #we need to check wheather profile pic is present, so data is not added to the db
            profile.user = user  #defines the one to one relation of user that is shown in models

            if 'profile_pic' in request.FILES: #
                profile.profile_pic = request.FILES['profile_pic']  #if we included pro pic we assign it to the db and request.FILES is actually a dict of all the files added to form

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors) #shows error if form is invalid
    
    else:
         user_form = UserForm()
         profile_form = UserExtra()

    return render(request, 'fraud/registration.html',context={'user_form':user_form , 'profile_form' :profile_form, 'registered':registered})

def user_login(request):

    if(request.method == 'POST'):
        username = request.POST.get('username')  #recieves username and password from the form
        password = request.POST.get('password')

        user = authenticate(username = username, password= password)  #user variable is a boolean which holds the value returned by builtin authenticate fn
           
        if user:
            if user.is_active:       #django checks if user is authenticated
                login(request,user)  #inbuilt function which logs in automatically
                return render(request,'fraud/landing.html')

            else:
                return HttpResponse('The Account is Currently Inactive')
            
        else:       #if user hasnt registered yet

            print("Username - {} and pswd - {}".format(username,password))      #outputs to console about details of invalid login attempts
            return HttpResponse('Invalid login details, Please Check if you have Registered')

    else:
        return render(request,'fraud/login.html')  #

@login_required                                         #decorator will only run this function if user has logged in
def user_logout(request):                   #logs out user
    logout(request)                                     #inbuilt function
    return HttpResponseRedirect(reverse('fraud:login'))

@login_required
def landing(request):

    return render(request, 'fraud/landing.html')

def check(request):

    form_data = Transaction_Details()
    if(request.method == 'post'):
        form_data = Transaction_Details(request.POST)

        if(form_data.is_valid):
            trans_form = form_data.save()
            trans_form.save()

        else:
            return HttpResponse('Invalid Form Values')

    else:
        return render(request, 'fraud/check.html', context= {'form' : form_data})

def result(request):

    return render(request, 'fraud/result.html')








