from dataclasses import field
from django import forms
from .models import Post

# Le indicamos a Django que PostForm es un formulario mediante forms.ModelForm.
class PostForm(forms.ModelForm):
    
    # Le decimos a Django qué modelo debe ser utilizado para crear este formulario.
    class Meta:
        model = Post
        # En este escenario sólo queremos title y text para ser mostrados - author 
        # será la persona que está conectada (¡tú!) y created_date se definirá 
        # automáticamente cuando creemos un post (es decir, en el código)
        fields = ('title', 'text')