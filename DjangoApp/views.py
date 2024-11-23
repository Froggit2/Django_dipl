from django.shortcuts import render
from .models import *
# Create your views here.


def glavn(request):
    return render(request, 'glavn.html')


def registr(request):
    login_input = request.POST.get('login')
    login_db = Users.objects.filter(login=login_input).get()
    password_1 = request.POST.get('password_1')
    password_2 = request.POST.get('password_2')
    if password_1 != password_2:
        error = 'Пароли должны совпадать!'
        return render(request, 'registr.html',
                      {'error': error})
    if login_input == login_db:
        error = 'Логин не должен совпадать с логином другого пользавателя!'
        return render(request, 'registr.html',
                      {'error': error})
    return render(request, 'registr.html')


def login_func(request):
    login_input = request.POST.get('login')
    password_input = request.POST.get('password')
    login_db = Users.objects.filter(login=login_input).get()
    password_db = Users.objects.filter(password=password_input).get()
    if login_input == login_db and password_input == password_db:
        message = 'Вы успешно вошли!'
        return render(request, 'login.html',
                      {'message': message})
    error = 'Неправильный логин или пароль'
    return render(request, 'login.html',
                  {'error': error})


def logout(request):
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