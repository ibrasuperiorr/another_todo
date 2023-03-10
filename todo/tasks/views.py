from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'tasks' : tasks, 'form' : form}
    return render(request, "tasks/list.html", context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,   instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form" : form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task' : task}

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'tasks/delete.html', context)