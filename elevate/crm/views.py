from django.shortcuts import render, redirect
from .models import Task, Review
from .forms import TaskForm

# Create your views here.

def home(request):

    return render(request, 'crm/index.html')



def task(request):
  
  queryDataAll = Task.objects.all()
  
  context = {
     'AllTasks': queryDataAll,
  }

  return render(request, 'crm/task.html', context)






def register(request):
    return render(request, 'crm/register.html')





def create_task(request):
    
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
        
            form.save()
        
            return redirect(task)
        
        else:
        
            print(form.errors)



    context = {'TaskForm': form}


    return render(request, 'crm/create-task.html', context )
