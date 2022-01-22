from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.conf import settings
from django.db import models
from django.utils import timezone

# Definimos el modelo, en este caso nuestro objeto.
class Post(models.Model): # models.Model: Significa que Post es un modelo de Djando, así que Django sabe que debe guardarlo en la base de datos.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # settings.AUTH_USER_MODEL devuelve una cadena (la ubicación del modelo de usuario)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now) #Guardamos la fecha de creación.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    # La opción related_name en models.ForeignKey nos permite acceder acceso a los comentarios desde el modelo Post.
    # Ayuda related_name = https://stackoverflow.com/questions/2642613/what-is-related-name-used-for
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text