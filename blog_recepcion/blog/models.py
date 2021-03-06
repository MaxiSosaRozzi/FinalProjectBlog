from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    sugerencia = models.TextField()
    nombre_de_huesped = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)

class AvatarBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)    