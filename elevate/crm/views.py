from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import HttpResponse

from .forms import TaskForm,CreateUserForm,LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout




# Create your views here.

def home(request):

    return render(request, 'crm/index.html')



# crud -reading data

def tasks(request):
  
  queryDataAll = Task.objects.all()
  context = {'AllTasks': queryDataAll}
  return render(request, 'crm/view-tasks.html', context)




def register(request):
    return render(request, 'crm/register.html')




# crud -creating data
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('views-tasks')

    context = {'TaskForm': form}
    return render(request, 'crm/create-task.html', context )



# CRUD - Updating data (view-tasks.html, update-task.html, views.py)
def update_task(request, pk):
    # task = Task.objects.get(id=pk)
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('views-tasks')

    context = {'UpdateTask': form}
    return render(request, 'crm/update-task.html', context )


#CRUD -DELETE TASK ()

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('views-tasks')

    # context = {'item': task}
    return render(request, 'crm/delete-task.html')

#CRUD - REGISTER USER (register.html, views.py)
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully')
        
    context = {'RegistrationForm': form}
    return render(request, 'crm/register.html', context )


#CRUD - LOGIN USER (login.html, views.py)

def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
    
        if form.is_valid():
            username = request.POST['username']
            password= request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(dashboard)
    
    context = {'LoginForm': form}

    return render(request, 'crm/my-login.html', context )




def dashboard(request):

    return render(request, 'crm/dashboard.html')
