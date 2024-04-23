from django.urls import path 
from . import views

app_name = 'demoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('test/<name>/<id>', views.test2, name='test2'),
    path('query/', views.queryview, name='queryview'),
    path('form/', views.showform, name='showform'),
    path('getform/', views.getform, name='getform'), 
    path('test404/', views.view404, name='404')
]

# handler404 = 'demoapp.views.view404'
