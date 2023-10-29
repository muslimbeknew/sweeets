from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def  homePage(request):
    return  HttpResponse("Asosiy sahifa")

def homePageNum(request,son):
    name= request.GET['name']
    age = request.GET['age']
    return HttpResponse(f'Salom{name} yosh {age}! ')
