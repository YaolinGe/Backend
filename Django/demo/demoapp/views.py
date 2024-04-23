from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseNotFound, Http404
from django.urls import reverse

def index(request):
    content = "<html><body><h1>Hello, world. This is the index view of DemoApp</h1></body></html>"
    return HttpResponse(content); 

def test(request): 
    path = request.path 
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.META['PATH_INFO']

    response = HttpResponse()
    response.headers['Age'] = 20
    reversed_URL = reverse('demoapp:test')

    msg = f"""<br>
    <br>Path: {path}
    <br>Scheme: {scheme}
    <br>Method: {method}
    <br>Address: {address}
    <br>User Agent: {user_agent}
    <br>Path Info: {path_info}
    <br> Response header: {response.headers}
    <br> Reversed URL: {reversed_URL}
    """

    return HttpResponsePermanentRedirect(reverse('demoapp:showform'))
    # return HttpResponse(msg, content_type='text/html', charset='utf-8')

def test2(request, name, id):
    return HttpResponse("Name: {} UserID: {}".format(name, id))

def queryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name: {} UserID: {}".format(name, id))

def showform(request): 
    return render(request, 'form.html')

def getform(request):
    if request.method == "POST": 
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse("Name: {} UserID: {}".format(name, id))

def view404(request): 
    # return HttpResponseNotFound("Page not found")
    # raise HttpResponse("404: Page not found!")
    # return HttpResponse("404: Page not found!")
    # content = "404: Page not found!"
    return HttpResponse("405: Page not found!"); 

def handler404(request):
    return HttpResponse("404: Page not found!")