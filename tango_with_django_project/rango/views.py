from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    link = "<br/> <a href='/rango/about'>About</a>"
    return HttpResponse("Rango says hey there world!" + link)

def about(request):
    link = "<br/> <a href='/rango'>main page</a>"
    student = "<br/>This tutorial has been put together by James Carroll, 2083013c"
    return HttpResponse("Rango says here is the about page." + link + student)

