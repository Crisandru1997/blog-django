from turtle import pos
from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Tenemos diferentes piezas en su lugar: el modelo Post está definido en models.py, 
# tenemos a post_list en views.py y la plantilla agregada. 
# ¿Pero cómo haremos realmente para que nuestros posts aparezcan 
# en nuestra plantilla HTML? Porque eso es lo que queremos, tomar 
# algún contenido (modelos guardados en la base de datos) y mostrarlo 
# adecuadamente en nuestra plantilla, ¿no?
# Esto es exactamente lo que las views se supone que hacen: conectar 
# modelos con plantillas. En nuestra view post_list necesitaremos tomar 
# los modelos que deseamos mostrar y pasarlos a una plantilla. 
# En una vista decidimos qué (modelo) se mostrará en una plantilla.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # render que reproduce (construye) nuestra plantilla blog/post_list.html.
    return render(request, 'blog/post_list.html', {'posts':posts})