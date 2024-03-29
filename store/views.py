from django.shortcuts import render, redirect
from store.models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from store.forms import SignUpForm, UpdateUserForm,ChangePasswordForm
from django import forms


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def about(request):
    return render(request, "about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully...!")
            return redirect("home")
        else:
            messages.success(request, "There was error, Please try again...!")
            return redirect("login")
    else:
        return render(request, "login_user.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully...!")
    return redirect("home")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # login in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Registered Successfully..!")
            return redirect("home")
        else:
            messages.error(request, "Error creating account.")
            return redirect("register_user")
    else:
        return render(request, "register_user.html", {"form": form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product": product})


def category(request, foo):
    # replace hyphens with spaces
    foo = foo.replace("-", " ")
    # grap the category
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        messages.success(request, "Categories Searching find Successfully..!")
        return render(
            request, "category.html", {"products": products, "category": category}
        )

    except:
        messages.success(request, "That Category Doesn't Exits..!")
        return redirect("home")


def category_summary(request):
    categories = Category.objects.all()
    return render(request, "category_summary.html", {"categories": categories})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "User has been update..!")
            return redirect("home")
        return render(request, "update_user.html", {"user_form": user_form})
    else:
        messages.success(request, "You Must Be Logged First..!")
        return redirect('home')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,  "Your Password Has Been Updated.")
                # logout(request, current_user)
                return redirect("login")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect("update_password")
        else:
            form = ChangePasswordForm(current_user)  # Fix typo here
            return render(request, "update_password.html", {"form": form})
    else:
        return redirect("home")










