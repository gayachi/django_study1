from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("heloo")
#HttpResponse only text available
# Create your views here.
#django view polls