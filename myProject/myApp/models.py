from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField 


class Productos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='productos/')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
            counter = 1
            while Productos.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.nombre)}-{counter}"
                counter += 1
        super().save(*args, **kwargs)


    def str(self):
        return self.nombre