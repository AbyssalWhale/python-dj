from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Represents main page of movies app. Index always must accept request


def index(request):

    return HttpResponse("Hello from orders view!!!")
