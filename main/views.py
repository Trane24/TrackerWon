from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from .forms import AddPostForm, RegisterUserForm
from .models import *


class IndexFile(generic.ListView):
    template_name = "main/main.html"
    context_object_name = "file"
    queryset = File.objects.filter(is_published=True)
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexFile, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class FileByCategory(generic.ListView):
    template_name = "main/main.html"
    context_object_name = "file"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FileByCategory, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context

    def get_queryset(self):
        slug = self.kwargs["slug"]
        return File.objects.filter(category__slug=slug, is_published=True)


class ShowFile(generic.DetailView):
    model = File
    template_name = "main/post.html"
    pk_url_kwarg = "file_id"
    context_object_name = "file"

    def get_context_data(self, **kwargs):
        context = super(ShowFile, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class CreateFile(generic.CreateView):
    form_class = AddPostForm
    template_name = "main/create_file.html"

    def get_context_data(self, **kwargs):
        context = super(CreateFile, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "main/login.html"
    
    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        return context


class RegisterUser(generic.CreateView):
    form_class = RegisterUserForm
    template_name = "main/register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


