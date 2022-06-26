from django.urls import URLPattern, path
from blog.views import BlogCreate, BlogList, BlogDetail, BlogUpdate, BlogDelete, BlogLogin, BlogLogout, About

urlpatterns = [
    path("",BlogCreate.as_view(),name="blog_create"),
    path('listar/',BlogList.as_view(),name="blog_list"),
    path("detalle/<pk>/",BlogDetail.as_view(),name="blog_detail"),
    path('editar/<pk>/',BlogUpdate.as_view(),name="blog_update"),
    path('borrar/<pk>/',BlogDelete.as_view(),name="blog_delete"),
    path("entrar/", BlogLogin.as_view(), name="blog_login"),
    path("salir/", BlogLogout.as_view(), name="blog_logout"),
    path("about/", About.as_view(), name="blog_about"),
]