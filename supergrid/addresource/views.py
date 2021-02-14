from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Choose a provder to add to the schdeule")