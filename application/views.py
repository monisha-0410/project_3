from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jampandu(request):
    return HttpResponse('hii jampandu u r mad')