from django.contrib import admin
from noticias_app.models import Noticia, Categoria
# Register your models here.

admin.site.register(Noticia)
admin.site.register(Categoria)