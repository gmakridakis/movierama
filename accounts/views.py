from django.contrib.auth.models import User
from django.shortcuts import redirect, render


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
            # messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            # messages.error(request, f"User with the username {username} already exists")
            return redirect("register")

        user = User.objects.create(
            username=username, first_name=first_name, last_name=last_name, password=password, email=email
        )
        user.save()
        return render(request, "movies/index")

    else:
        return render(request, "accounts/register.html")
