from django.urls import URLPattern, path
from blog.views import *

urlpatterns = [
    path("",BlogCreate.as_view(),name="blog_create"),
    path('listar/',BlogList.as_view(),name="blog_list"),
    path("<pk>/",BlogDetail.as_view(),name="blog_detail"),
    path('editar/<pk>/',BlogUpdate.as_view(),name="blog_update"),
    path('borrar/<pk>/',BlogDelete.as_view(),name="blog_delete"),
]