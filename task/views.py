from django.shortcuts import render,redirect 
from .models import *
from .forms import *
# Create your views here.

def home(request):
    tasks = Task.objects.all()
    forms = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'tasks':tasks, 'forms':forms}
    return render(request, 'task/home.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form}
    return render(request, 'task/update.html', context)

def delete(request, pk):
    item = Task.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    context = {'item':item}
    return render(request, 'task/delete.html', context)

def clear(request):
    task = Task.objects.all()
    context = {'task':task}
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request,'task/clear.html',context)