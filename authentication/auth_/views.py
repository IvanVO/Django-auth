from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .models import *
from .forms import *

def home(request):

    return HttpResponse("Home Page")

def registrationPage(request):
    # step 1 : Create form
    form = CreateUserForm()
    # step 2 : Check the request method
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # step 3 : Check if the form submition is valid.
        if form.is_valid():
            # step 4 : Save the form/user.
            user = form.save()
            # step 5 : Retrieve the username without retreving any other form data.
            username = form.cleaned_data.get('username')

            print(f"User with {username} was successfully created")

            return redirect('login')
            # return redirect('/')
    context = {'form': form}

    return render(request, "users/register.html", context)


def loginPage(request):
    # step 1 : Check the request method
    if request.method == 'POST':
        # step 2 : Assign the values username & password to variables with the same name.
        # --> The parameter passed into the get('str') is the value of the name property in the input tag in the form from 'login.html'
        username = request.POST.get('username')
        password = request.POST.get('password')

        # step 3 : Authenticate user
        user = authenticate(request, username=username, password=password)

        # step 4 : Log in the user if he/she was successfully autheticated
        if user is not None:
            login(request, user)
            print("user logged in")
            return redirect('/')
        else:
            print("Username or Password is incorrect")

    return render(request, "users/login.html")


# TODO: Add logout view
