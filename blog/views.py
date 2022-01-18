from django.shortcuts import render

def post_list(request):
    # render que reproduce (construye) nuestra plantilla blog/post_list.html.
    return render(request, 'blog/post_list.html', {})