from django.shortcuts import render
from .models import *

# Create your views here.
Users_db = Users.objects


def glavn(request):
    return render(request, 'glavn.html')


def register(request):
    if request.method == "POST":
        login_input = request.POST.get('login')
        login_db = Users_db.filter(login=login_input).get()
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if password_1 != password_2:
            error = 'Пароли должны совпадать!'
            return render(request, 'register.html',
                          {'error': error})
        if login_input == login_db:
            error = 'Логин не должен совпадать с логином другого пользавателя!'
            return render(request, 'register.html',
                          {'error': error})
        Users_db.create(login=login_input, password=password_2)
        return render(request, 'register.html')
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        login_input = request.POST.get('login')
        password_input = request.POST.get('password')
        try:
            login_db = Users.objects.get(login=login_input)
            password_db = Users.objects.get(password=password_input)
            message = 'Вы успешно вошли!'
            return render(request, 'login.html',
                          {'message': message})
        except:
            error = 'Неправильный логин или пароль'
            return render(request, 'login.html',
                          {'error': error})
    return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        login_input = request.POST.get('login')
        password_input = request.POST.get('password')
        login_db = Users.objects.filter(login=login_input).get()
        password_db = Users.objects.filter(password=password_input).get()
        if login_input == login_db and password_input == password_db:
            login_db.delete()
            password_db.delete()
            message = 'Вы успешно вышли!'
            return render(request, 'logout.html', {'message': message})
        error = 'Неправильный логин или пароль!'
        return render(request, 'logout.html',
                      {'error': error})
    return render(request, 'logout.html')
