from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import Task


def Home(request):
    task = Task.objects.all()

    context = {
        'task': task,
    }

    return render(request, 'view_task.html', context)


def ADD_TASK(request):
    return render(request, 'add_task.html')


def SAVE_TASK(request):
    if request.method == "POST":
        task_title = request.POST.get('title')
        task_desc = request.POST.get('description')

        task = Task(
            taskTitle=task_title,
            taskDesc=task_desc,
        )

        task.save()
        return redirect('home')


def DELETE_TASK(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')
