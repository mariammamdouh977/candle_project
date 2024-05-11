from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import auth, messages

# Create your views here.


def index(request):
    return render(request, "playground/index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid login details please try again")

    return render(request, "playground/login.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            return render(request, "playground/signup.html", {"form": form})
    else:
        form = UserCreationForm()
    return render(request, "playground/signup.html", {"form": form})


def products(request):
    return render(request, "playground/products.html")


def forgetPassword(request):
    return render(request, "playground/forgetPassword.html")


def checkout(request):
    return render(request, "playground/checkout.html")


def learnmore(request):
    return render(request, "playground/learnmore.html")
