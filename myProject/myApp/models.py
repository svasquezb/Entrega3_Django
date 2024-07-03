from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField 

class Productos(models.Model):
    nombre = models.CharField(max_length=400)
    precio = models.FloatField(max_length=10, default=0.0)
    imagen = models.ImageField(null=True, blank=True, upload_to="Productos/",default="productos/producto-default.png")
    descripcion = RichTextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, max_length=400)
    creado = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('producto-detail', kwargs={'pk':self.pk, 'slug':self.slug})

    def save(self, *args, **kwargs):
        value = self.nombre ##Revisar estoo     
        self.slug = slugify(value, allow_unicode=True)  
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.nombre, self.creado)