# Importaciones
from ast import If
from turtle import pos
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

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
    posts = Post.objects.all().order_by('published_date')
    # render que reproduce (construye) nuestra plantilla blog/post_list.html.
    return render(request, 'blog/post_list.html', {'posts':posts})

# def post_detail (request, pk): Tenga en cuenta que necesitamos usar exactamente 
# el mismo nombre que el que especificamos en urls (pk). ¡Omitir esta variable es 
# incorrecto y resultará en un error!
def post_detail(request, pk):
    
    # No captura el error en caso de que el post no exista.
    # post = Post.objects.get(pk=pk)
    
    # Django tiene una función que se encarga de esto: get_object_or_404
    # en caso de que no haya ningún post con el pk se mostrara una pagina mas agradable (Page Not Found 404).
    # Lo bueno es que podemos crear nuestra propia pagina error 404, pero aqui no lo haremos.
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    # Cuando enviamos el formulario somos redirigidos a la misma vista, 
    # pero esta vez tenemos algunos datos adicionales en request, 
    # más específicamente en request.POST
    
    # Cuando enviamos el formulario somos redirigidos a la misma vista, 
    # pero esta vez tenemos algunos datos adicionales en request, 
    # más específicamente en request.POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        # Lo siguiente es verificar si el formulario está correcto 
        # (si todos los campos necesarios están definidos y no hay valores incorrectos). 
        # Lo hacemos con form.is_valid().
        if form.is_valid():
            post = form.save(commit=False) 
            # commit=False significa que no queremos guardar el modelo 
            # Post aún - queremos añadir la autora primero. 
            # La mayoría de las veces utilizarás form.save(), sin commit=False.
            # , pero en este caso, tenemos que hacerlo. post.save() 
            # conservará los cambios (añadiendo a autor) y se creará una nuevo post en el blog!
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    # Segundo: obtenemos el modelo Post que queremos editar con 
    # get_object_or_404(Post, pk=pk) y después, al crear el formulario
    # pasamos este post como una instancia tanto al guardar el formulario…
    post = get_object_or_404(Post,pk=pk)
    if request.POST:
        # ... y justo cuando abrimos un formulario con este post para editarlo:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})
