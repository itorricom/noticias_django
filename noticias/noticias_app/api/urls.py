from django.urls import path
from noticias_app.api.views import noticia_listado, noticia_buscar_id,categoria_listado,categoria_buscar_id

urlpatterns = [
    path('listado/', noticia_listado, name='noticia-listado'),
    path('<int:id>', noticia_buscar_id, name='noticia-buscar-id'),
    path('categoria/', categoria_listado, name='categoria'),
    path('categoria/<int:id>', categoria_buscar_id, name='categoria-buscar-id'),
]