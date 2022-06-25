from django.shortcuts import render

from msilib.schema import ListView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import BlogModel

class BlogList(ListView):

    model = BlogModel
    template_name = "blog/blog_list.html"

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
