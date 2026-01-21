from django.shortcuts import redirect, render
from django.http import HttpResponse
from httpx import request
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, "home.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)

            role = user.userprofile.role

            if role == "citizen":
                return redirect("index")
            elif role == "municipality":
                return redirect("municipalitypage")
            elif role == "truck_operator":
                return redirect("truck_dashboard")
            elif role == "factory":
                return redirect("factory_interface")
            else:
                return redirect("home")

        else:
            messages.error(request, "Invalid email or password")

    return render(request, "login.html")


from .models import UserProfile

def signup_view(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, "signup.html")

        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists")
            return render(request, "signup.html")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=fullname
        )

        UserProfile.objects.create(
            user=user,
            role=role
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "signup.html")

def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")

def map_view(request):
    return render(request, "map.html")

def report(request):
    return render(request, "report.html")

def analytics(request):
    return render(request, "analytics.html")

def about(request):
    return render(request, "about.html")



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not all([name, email, subject, message]):
            messages.error(request, "All fields are required.")
            return redirect("contact")

        messages.success(request, "Message sent successfully")
        return redirect("contact")

    return render(request, "contact.html")




def municipalitypage(request):
    return render(request, "municipalitypage.html")

def truck_dashboard(request):
    return render(request, "truck_dashboard.html")

def factory_interface(request):
    return render(request, "factory_interface.html")

def bins_view(request):
    return render(request, "Smart_bins.html")

def collection(request):
    return render(request, "collection.html")



