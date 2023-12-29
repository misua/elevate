from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):

    return render(request, 'crm/index.html')



# crud -reading data

def tasks(request):
  
  queryDataAll = Task.objects.all()
  queryRecent = Task.objects.all().latest('created')
  context = {'AllTasks': queryDataAll,'RecentTasks': queryRecent}
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


#CRUD -DELETE TASK

def delete_task(request, pk):
    task = get_object_or_404(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('views-tasks')

    context = {'item': task}
    return render(request, 'crm/delete-task.html', context)