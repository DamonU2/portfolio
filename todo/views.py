from django.shortcuts import render, redirect, get_object_or_404
from .models import To_Do, Step

def todo_home(request):
    todo_incomplete = To_Do.objects.filter(complete=False)
    todo_complete = To_Do.objects.filter(complete=True)
    steps_incomplete = Step.objects.filter(complete=False)
    steps_complete = Step.objects.filter(complete=True)
    return render(request, 'todo/index.html', {
        'incomplete': todo_incomplete, 'complete': todo_complete,
        'inc_step': steps_incomplete, 'com_step': steps_complete})

def todo_add(request):
    todo = To_Do()
    todo.text = request.POST['todoitem']
    todo.save()
    return redirect('todo_home')

def todo_add_step(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(To_Do, pk=pk)
        step = Step()
        step.text = request.POST['todostep']
        step.to_do_id = todo
        step.save()
    return redirect('todo_home')

def todo_complete(request, pk):
    todo = get_object_or_404(To_Do, pk=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_home')

def todo_complete_step(request, pk):
    step = get_object_or_404(Step, pk=pk)
    step.complete = True
    step.save()
    return redirect('todo_home')

def todo_delete_step(request, pk):
    step = get_object_or_404(Step, pk=pk)
    step.delete()
    return redirect('todo_home')

def todo_uncheck(request, pk):
    todo = get_object_or_404(To_Do, pk=pk)
    todo.complete = False
    todo.save()
    return redirect('todo_home')

def todo_delete(request, pk):
    todo = get_object_or_404(To_Do, pk=pk)
    todo.delete()
    return redirect('todo_home')