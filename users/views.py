from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


def login_user(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("users:profiles")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # проверяем, что существует
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exists")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("users:profiles")
        else:
            messages.error(request, "Username OR password is incorrect")
    return render(request, "users/login_register.html")


def logout_user(request):
    logout(request)
    messages.error(request, "User was logged out!")
    return redirect("users:login")


def register_user(request):
    page = "register"
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    # то есть исключаем скилы у которых нету описания
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")
    context = {
        "profile": profile,
        "top_skills": top_skills,
        "other_skills": other_skills,
    }
    return render(request, "users/user_profile.html", context)
