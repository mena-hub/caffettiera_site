from django.db.models import Model, CharField, TextField, DateTimeField, SmallIntegerField
from ckeditor.fields import RichTextField

class Page(Model):
    title = CharField(max_length=200, verbose_name="título")
    content = RichTextField(verbose_name="contenido")
    ordering = SmallIntegerField(default=0, verbose_name="orden")
    created = DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['ordering', 'title']
    
    def __str__(self):
        return self.title