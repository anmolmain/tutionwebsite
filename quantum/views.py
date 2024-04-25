from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect
from .forms import LowerSchoolStudentForm
from .forms import MiddleSchoolStudentForm
from .forms import HighSchoolStudentForm
from .forms import ContactForm
from .forms import HomePageContactForm

def contact_homepage(request):
    if request.method == 'POST':
        form = HomePageContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('/formsubmitted')  # Redirect to the home page or a thank you page
        else:
            messages.error(request, 'Form submission failed. Please check the form.')
    else:
        form = HomePageContactForm()
    
    return render(request, 'home.html', {'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/formsubmitted')  # Redirect to the home page or a thank you page
        else:
            print(form.errors)  # Print form errors to the console
            messages.error(request, 'Form submission failed. Please check the form.')
    else:
        form = ContactForm()
    
    return render(request, 'home.html', {'form': form})

def success(request):
    return render(request, 'home.html')


def high_school_registration(request):
    if request.method == "POST":
        form = HighSchoolStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pricing')  # Redirect to the home page or a thank you page
    else:
        form = HighSchoolStudentForm()   
    context = {'form': form}
    return render(request, 'home.html', context)


def middle_school_registration(request):
    if request.method == "POST":
        form = MiddleSchoolStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pricing')  # Redirect to the home page or a thank you page
    else:
        form = MiddleSchoolStudentForm()
    context = {'form': form}
    return render(request, 'home.html', context)


def lower_school_registration(request):
    if request.method == "POST":
        form = LowerSchoolStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pricing')  # Redirect to the home page or a thank you page
    else:
        form = LowerSchoolStudentForm()
    context = {'form': form}
    return render(request, 'home.html', context)


def home(request):
    return render(request, 'home.html')

def login(request):
    try:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Invalid Credential")
                return redirect("login")
        else:
            return render(request, "login.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("login")

# Register view to register user
def register(request):
    try:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already exist")
                    return redirect("register")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email already registered")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password1,
                    )
                    user.save()
                    return redirect("login")
            else:
                messages.info(request, "Password not matches")
                return redirect("register")
        else:
            return render(request, "register.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("register")

# Logout view to logout user
def logout(request):
    try:
        auth.logout(request)
        return redirect("/")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("/")

def about(request):
    return render(request, 'about.html')

def enroll(request):
    return render(request, 'enroll.html')

def lowerschool(request):
    return render(request, 'lowerschool.html')

def middleschool(request):
    return render(request, 'middleschool.html')

def highschool(request):
    return render(request, 'highschool.html')

def contactus(request):
    return render(request, 'contactus.html')

def formsubmitted(request):
    return render(request, 'formsubmitted.html')

def pricing(request):
    return render(request, 'pricing.html')

