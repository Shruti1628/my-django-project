from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name='index'),
    path('ME',views.about,name='about'),
    path('Nice',views.projects,name='project'),
    path('Number',views.contact,name='contact'),
     
    ]


