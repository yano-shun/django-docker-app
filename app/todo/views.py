from django.shortcuts import render, redirect
from .models import Task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # 簡略化のため。セキュリティ強化時には削除を検討。
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')

    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})
