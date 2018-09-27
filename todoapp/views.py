from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Main routes
def index(request):
    if request.method == "GET":
        # Display all the todos:
        return HttpResponse('index GET')
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
    return HttpResponse('signup')

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')
