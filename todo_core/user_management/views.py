from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import User

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pw = request.POST.get("password")
        pw2 = request.POST.get("password2")

        if pw != pw2:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
        if len(username) < 4:
            messages.error(request, "At least 4 characters!")
            return redirect("register")
        
        if len(email) < 6:
            messages.error(request, "At least 6 characters!")
            return redirect("register")
        
        if not User.object.filter(username=username).exists():
            messages.error(request, "User exists")
            return redirect("register")
        
        User.objects.create_user(username=username, email=email, password=pw)
        return redirect("login")
    return render(request, "registration/register.html")