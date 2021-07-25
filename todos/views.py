from django.http.response import HttpResponseRedirect
from .models import TableOfTodo, Todo
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class TodoMainView(ListView):
    model = TableOfTodo
    template_name = "todos/main_index.html"



class IndexView(ListView):
    model = Todo
    template_name = 'todos/sub_index.html'

    def get_queryset(self): #QuerySet - custmizing
        return Todo.objects.all().order_by('due')


class AllView(ListView):
    model = Todo
    template_name = 'todos/show_all.html'

    def get_queryset(self): #QuerySet - custmizing
        return Todo.objects.all().order_by('due')


class Add(TemplateView):
    model = Todo
    template_name = 'todos/add.html'


class DetailList(ListView):
    model = Todo
    template_name = 'todos/details.html'


class DetailedView(DetailView):
    model = Todo
    template_name = 'todos/details_2.html'


class Delete(ListView):
    model = Todo
    template_name = 'todos/delete.html'


class Modify(ListView):
    model = Todo
    template_name = 'todos/modify.html'
    
    def get_queryset(self): #QuerySet - custmizing
        return Todo.objects.all().order_by('due')



def add(request):
    added_todo = Todo(title = request.POST['title'], contents=request.POST['contents'], due=request.POST['due'])
    added_todo.save()
    return HttpResponseRedirect(reverse('todos:add'))


def delete(request):
    delete_todo = Todo.objects.get(pk=request.POST['data_delete'])
    delete_todo.delete()
    return HttpResponseRedirect(reverse('todos:delete'))


def modify_1(request):
    object = Todo.objects.get(pk=request.POST['modify_id'])
    context = {'object':object}
    return render(request, 'todos/modify_2.html', context)


def modify_2(request):
    object = Todo.objects.get(pk=request.POST['modify_id'])
    object.title = request.POST['title']
    object.contents=request.POST['content']
    object.due=request.POST['due']
    object.save()
    return HttpResponseRedirect(reverse('todos:modify'))