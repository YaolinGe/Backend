from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = "<html><body><h1>Hello, world. This is the index view of DemoApp</h1></body></html>"
    return HttpResponse(content); 


