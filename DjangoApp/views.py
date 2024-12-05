from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .models import Users, Products

# Create your views here.

Users_db = Users.objects
Products_db = Products.objects

def glavn(request):
    return render(request, 'glavn.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        name_input = request.POST.get('name')
        price_input = request.POST.get('price')
        Products_db.create(name=name_input, price=price_input)
        message = 'Продукт успешно добавлен!'
        return render(request, 'add_product.html', {'message': message})
    return render(request, 'add_product.html')


def products(request):
    products = Products_db.all()
    return render(request, 'products.html', {'products': products})

def login(request):
    if request.method == "POST":
        login_input = request.POST.get('login')
        password_input = request.POST.get('password')
        user = authenticate(request, username=login_input, password=password_input)
        if user is not None:
            auth_login(request, user)
            message = 'Вы успешно вошли!'
            return render(request, 'login.html', {'message': message})
        else:
            error = 'Неправильный логин или пароль'
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')