from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from blog.models import BlogModel
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views import View

class BlogList(ListView):

    model = BlogModel
    template_name = "blog/blog_list.html"

def Vista1(request):
    diccionario = {}
    return render(request,"blog/blog_list.html",context=diccionario) 

      
class BlogDetail(DetailView):

    model = BlogModel
    template_name = "blog/blog_detail.html"

class BlogCreate(CreateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo","nombre_de_huesped","sugerencia"]

class BlogUpdate(UpdateView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")
    fields = ["titulo","nombre_de_huesped","sugerencia"]

class BlogDelete(DeleteView):

    model = BlogModel
    success_url = reverse_lazy("blog_list")

class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

class About(View):
   
 def get(self, request, *args, **kwargs):
  return render(request, "blog/blog_about.html", {} )

 def post():
  pass  
