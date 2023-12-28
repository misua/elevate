from django.shortcuts import render
from .models import Task, Review
from .forms import TaskForm

# Create your views here.

def home(request):

    return render(request, 'crm/index.html')



def task(request):
  
  #queryDataSingle = Task.objects.all()
  queryDataSingle = Task.objects.filter(title__contains='buy')

  context = {
     'singleTask': queryDataSingle,
  }

  return render(request, 'crm/task.html', context)




def register(request):
    return render(request, 'crm/register.html')




def task_form(request):
    
    form = TaskForm()

    context = {'TaskForm': form}


    return render(request, 'crm/task-form.html', context )
