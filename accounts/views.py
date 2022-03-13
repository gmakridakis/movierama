from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        # Validations
        if password != password2:
            print("Passwords do not match")
            messages.error(request, "Passwords do not match")
            return HttpResponseRedirect(reverse("register"))

        if User.objects.filter(username=username).exists():
            print(f"User with username {username} already exists")
            messages.error(request, f"User with username {username} already exists")
            return HttpResponseRedirect(reverse("register"))

        user = User.objects.create_user(
            username=username, first_name=first_name, last_name=last_name, password=password, email=email
        )
        user.save()
        auth.login(request, user)
        print(f"Welcome to Movierama {username}!")
        messages.success(request, f"Welcome to Movierama {username}!")
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "accounts/register.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        print("You have logged out from Movierama")
        messages.success(request, "You have logged out from Movierama")
        return HttpResponseRedirect(reverse("index"))


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print(f"Successful login")
            messages.success(request, f"Successful login")
            return HttpResponseRedirect(reverse("index"))
        else:
            print("Invalid credentials, check your username and password and try again")
            messages.error(request, "Invalid credentials, check your username and password and try again")
            return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "accounts/login.html")
