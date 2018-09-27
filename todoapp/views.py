from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Main routes
def index(request):
    if request.method == "GET":
        # Display all the todos:
        return render(request, 'todoapp/index.html')
    elif request.method == "POST":
        # Add a new todo
        return HttpResponse('index POST')

def delete(request, todo_id):
    # Delete a todo
    return HttpResponse("Delete this")

def done():
    # will mark a todo as complete
    return HttpResponse('done')

# Auth-related routes
def signup(request):
    if request.method == 'GET':
        return render(request, 'todoapp/signup.html')
    elif request.method == 'POST':
        return HttpResponse('POST to /signup')

def login(request):
    if request.method == 'GET':
        return render(request, 'todoapp/login.html')
    elif request.method == 'POST':
        return HttpResponse('posignup')

def logout(request):
    return HttpResponse('logout')
