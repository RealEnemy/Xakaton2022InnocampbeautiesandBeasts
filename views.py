from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def create(request):
    return render(request, 'main/create')


def join(request):
    return render(request, 'main/join')


def regi(request):
    return render(request, 'main/registration.html')


def login(request):
    return render(request, 'main/login.html')