from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, DetailView

from todoapp.forms import todoForms
from todoapp.models import task


def index(request):
    tlist = task.objects.all()
    if request.method == 'POST':
        name = request.POST['task']
        priority = request.POST['priority']
        date = request.POST['date']
        todo = task(task=name, priority=priority, date=date)
        todo.save()

    return render(request, 'index.html', {'tlist': tlist})


def delete(request, id):
    if request.method == 'POST':
        tlist = task.objects.get(id=id)
        tlist.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    tlist = task.objects.get(id=id)
    form = todoForms(request.POST or None, instance=tlist)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'tlist': tlist})

#
# class Tasklistview(ListView):
#     model = task
#     template_name = 'index.html'
#     context_object_name = 'tlist'
#
#
# class Taskdeleteview(DeleteView):
#     model = task
#     template_name = 'delete.html'
#     success_url = reverse_lazy('todoapp:home')
#
# class Taskupdateview(UpdateView):
#     model=task
#     template_name = 'update.html'
#     context_object_name = 'tlist'
#     fields = ('name','priority','date')
#
#     def get_success_url(self):
#         return reverse_lazy('todoapp:home',kwargs='pk')
#
#
# class Taskdetailview(DetailView):
#     model=task
#     template_name = 'detail.html'
#     context_object_name = 'tlist'
