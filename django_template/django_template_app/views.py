from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView, 
    ListView, 
    DetailView
)
from django.urls import reverse_lazy
from .models import UserProfile, Request
from .forms import UserProfileForm, RequestForm


from django.shortcuts import render

# Create your views here.


# def create_user(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST)

#         if form.is_valid():
#             user = User.objects.create()
#             form.save(user=user)

#             return redirect("success_url")

#     else:
#         form = UserProfileForm()

#     return render(request, 'django_template_app/user_create_form.html')


class UserCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'django_template_app/user_create_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'django_template_app/user_update_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = UserProfile
    template_name = 'django_template_app/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class UserListView(ListView):
    model = UserProfile
    template_name = 'django_template_app/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = UserProfile
    template_name = 'django_template_app/user_detail.html'
    context_object_name = 'user'



# class ProjectCreateView(CreateView):
#     model = Project
#     form_class = ProjectForm
#     template_name = 'django_template_app/project_create_form.html'
#     success_url = reverse_lazy('project_list')

# class ProjectUpdateView(UpdateView):
#     model = Project
#     form_class = ProjectForm
#     template_name = 'django_template_app/project_update_form.html'
#     success_url = reverse_lazy('project_list')

# class ProjectDeleteView(DeleteView):
#     model = Project
#     template_name = 'django_template_app/project_confirm_delete.html'
#     success_url = reverse_lazy('project_list')

# class ProjectListView(ListView):
#     model = Project
#     template_name = 'django_template_app/project_list.html'
#     context_object_name = 'projects'

# class ProjectDetailView(DetailView):
#     model = Project
#     template_name = 'django_template_app/project_detail.html'
#     context_object_name = 'project'




    
