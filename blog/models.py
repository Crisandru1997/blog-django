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