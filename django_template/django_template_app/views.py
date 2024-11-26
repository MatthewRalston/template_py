from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView, 
    ListView, 
    DetailView
)
from django.urls import reverse_lazy
from .models import Author, Book
from .forms import AuthorForm, BookForm


from django.shortcuts import render

# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'my_app/user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'my_app/user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'my_app/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class UserListView(ListView):
    model = User
    template_name = 'my_app/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'my_app/user_detail.html'
    context_object_name = 'user'



class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'my_app/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'my_app/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'my_app/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

class ProjectListView(ListView):
    model = Project
    template_name = 'my_app/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'my_app/project_detail.html'
    context_object_name = 'project'




    
