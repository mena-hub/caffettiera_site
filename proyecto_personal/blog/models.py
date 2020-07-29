from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor import fields

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="título")
    content = fields.RichTextField(verbose_name="contenido")
    image = models.ImageField(blank=True, null=True, upload_to='blog', verbose_name="imagen")
    published = models.DateTimeField(default=now, verbose_name="fecha de publicación")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="autor")
    categories = models.ManyToManyField(Category, related_name="get_posts", verbose_name="categorías")

    class Meta:
        verbose_name = "posteo"
        verbose_name_plural= "posteos"
        ordering = ['-created']

    def __str__(self):
        return self.title