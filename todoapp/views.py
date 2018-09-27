from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Main routes
def index(request):
    todos = Todo.objects.all().order_by('text')
    users = User.objects.all()
    
    if request.method == "GET":
        # Display all the todos:
       
        return render(request, 
            'todoapp/index.html',
            {
                'todos': todos,
                'users': users
            })
    elif request.method == "POST":
        print("POST")
        # Add a new todo
        try: 
            user_id = request.POST['userid']
        except:
            return render(request,
                'todoapp/index.html',
                {
                    'error': 'You must select a user',
                    'todos': todos,
                    'users': users
                })
        else:
            new_todo = Todo()
            new_todo.text = request.POST['text']
            new_todo.user = User.objects.get(pk=user_id)
            new_todo.save()
            return redirect('index')

    return HttpResponse('index POST')

def delete(request, todo_id):
    # Delete a todo
    Todo.objects.get(id=todo_id).delete()
    return redirect('index')

def done(request, todo_id):
    # will mark a todo as complete
    item = Todo.objects.get(id=todo_id)
    item.is_complete = True
    item.save()
    return redirect('index')

# Auth-related routes
def signup(request):
    if request.method == 'GET':
        return render(request, 'todoapp/signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        try:
            user = User.objects.create_user(username=username, 
                password=password, 
                first_name = firstname,
                last_name = lastname)
            if user is not None:
                # auth.login(request, user)
                return login(request)
        except:
            return render(request, 'todoapp/signup.html', { 'error': 'Arggggg!' })
        return HttpResponse('POST to /signup')

def login(request):
    if request.method == 'GET':
        return render(request, 'todoapp/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:            
            return render(request, 'todoapp/login.html', { 'error': 'Invalid credentials' })

def logout(request):
    auth.logout(request)
    return redirect('index')
