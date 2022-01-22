
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # r: especifica que es una cadena regular sin formato. (https://www.delftstack.com/es/howto/python/python-r-before-string/)
    # ^: significa el comienzo.
    # $: indica el final.
    # <pk>: infica la clave principal.
    # \d: coincide con [0-9] y otros caracteres de dígitos.
    # +: significa que debe haber al menos 1 o mas digitos en el numero.
    
    # re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    # re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    # re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    
    # Seria lo mismo que lo anterior.
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]