
from django.shortcuts import render, HttpResponse
from home.models import task

# Create your views here.


def home(request):
    context = {'success' :False}
    
    if request.method == "POST":
        # Form handling
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = task(taskTitle=title, taskDesc=desc)
        ins.save()

    return render(request, 'index.html', context)


def tasks(request):
    allTasks = task.objects.all()
    # print(allTasks)
    # for i in allTasks:
    #     print(i.taskDesc)
    context = {'tasks': allTasks}
    
    return render(request, 'tasks.html', context)
