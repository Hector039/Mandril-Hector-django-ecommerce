from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(req):
    return render(req, "home.html")

def signIn(req):
    if req.method == "POST":
        try:
            user = authenticate(req, email=req.POST['username'], password=req.POST['password'])
        except Exception as error:
            render(req, "signin.html", {"form": AuthenticationForm, "error": error})

        if user is None:
            return render(req, "signin.html", {"form": AuthenticationForm, "error": "User name o password incorrect"})
        else:
            login(req, user)
            return redirect('home')

    return render(req, "signIn.html", {"form": AuthenticationForm})

def signUp(req):
    if req.method == "POST":
        if req.POST["password1"] == req.POST["password2"]:
            try:
                CustomUser.objects.create_user(first_name = req.POST["first_name"], last_name = req.POST["last_name"], email = req.POST["email"], password = req.POST["password1"], age = req.POST["age"])
                return redirect('home')
            except IntegrityError:
                return render(req, "signup.html", {"form": CustomUserCreationForm, "error": "You must be over 18 years old to register"})
        else:
            return render(req,"signup.html", {"form": CustomUserCreationForm, "error": "Passwords must be equals"})
    return render(req, "signUp.html", {"form": CustomUserCreationForm})

def closeSession(req):
    logout(req)
    return redirect('home')
