from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post) # Incluimos el Post en el panel de administración.
admin.site.register(Comment)
