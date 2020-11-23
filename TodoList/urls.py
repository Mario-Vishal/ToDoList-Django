"""TodoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('delete/<int:todo_pk>',views.delete,name="delete"),
    path('completed/<int:todo_pk>',views.completed,name="completed"),
    path('important/<int:todo_pk>',views.important,name="important"),
    path('viewimportant',views.viewimportant,name="viewimportant"),
    path('alltodo',views.alltodo,name="alltodo"),
    path('viewcompleted',views.viewcompleted,name="viewcompleted"),
    path('signupuser',views.signupuser,name="signupuser"),
    path('loginuser',views.loginuser,name="loginuser"),
    path('logoutuser',views.logoutuser,name="logoutuser"),
    path('addtodo',views.addtodo,name="addtodo")
]


