
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks=Task.objects.all().order_by('-updated_at')
    completed_task=Task.objects.filter(is_completed=True)
    print(completed_task)
    context={
        'tasks': tasks,
    }

    return render (request,'home.html',context)
