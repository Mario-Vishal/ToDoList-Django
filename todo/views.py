from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Todo
from django.http import HttpResponseRedirect

#authorization
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

#forms
from .forms import TodoForm

def home(request):

    if request.user.is_authenticated:
        return redirect('alltodo')
    
    return render(request,'todo/index.html')


def signupuser(request):

    if request.method == "GET":

        return render(request,'todo/signupuser.html',{'form':UserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('alltodo')
            except IntegrityError:
                return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'Username taken, try another!'})

        else:
            return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':"Passwords didn't match"})


def loginuser(request):

    if request.method == "GET":
        return render(request,'todo/loginuser.html',{'form':AuthenticationForm()})
    else:
        uname = request.POST['username']
        passkey = request.POST['password']
        user = authenticate(request,username = uname,password = passkey)
        if user is None:
            return render(request,'todo/loginuser.html',{'form':AuthenticationForm(),'error':"user credentials are wrong!"})

        else:
            login(request,user)
            return redirect('alltodo')

@login_required
def logoutuser(request):
    if request.method=="POST":
        logout(request)
        return redirect('home')


@login_required
def delete(request,todo_pk):
    
    if request.method == "POST":
        todo = get_object_or_404(Todo,pk=todo_pk)
        todo.delete()
        return HttpResponseRedirect(request.path_info)
    else:
        return redirect('alltodo')

@login_required
def completed(request,todo_pk):
    if request.method=="POST":
        todo = get_object_or_404(Todo,pk=todo_pk,user=request.user)
        if todo.completed:
            todo.completed=False
        else:
            todo.completed = True
        todo.save()
        return HttpResponseRedirect(request.path_info)
    else:
        return redirect('alltodo')

@login_required
def important(request,todo_pk):
    if request.method=="POST":
        todo = get_object_or_404(Todo,pk=todo_pk,user=request.user)
        if todo.important:
            todo.important=False
        else:
            todo.important = True
        todo.save()
        return HttpResponseRedirect(request.path_info)

    else:

        return redirect('alltodo')


@login_required
def alltodo(request):
    todos = Todo.objects.filter(user=request.user)
    
    if request.method == "GET":
        
        return render(request,'todo/alltodo.html',{'todos':todos})
    else:

        return render(request,'todo/alltodo.html',{'todos':todos,'error':'only max of 250 characters allowed!'})

@login_required
def addtodo(request):

    if request.method == "POST":
        todo = Todo()
        item =  request.POST['todo-input']
        if item=="":
            return redirect('alltodo')
        todo.user = request.user
        todo.todo_item = item
        todo.save()
        return redirect('alltodo')
    
@login_required
def viewcompleted(request):

    if request=="POST":
        return redirect('home')
    else:
        todos = Todo.objects.all().filter(user=request.user,completed=True)
        return render(request,'todo/completed.html',{'todos':todos})

@login_required
def viewimportant(request):
    if request=="POST":
        return redirect('home')
    else:
        todos = Todo.objects.all().filter(important=True,completed=False,user=request.user)
        return render(request,'todo/important.html',{'todos':todos})




    





