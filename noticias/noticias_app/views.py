# from django.shortcuts import render
# from noticias_app.models import Noticia
# from django.http import JsonResponse
# # Create your views here.
# def noticia_listado(request):
#     noticias = Noticia.objects.all()
#     data ={
#         'noticias': list(noticias.values())
#     }
#     return JsonResponse(data)

# def noticia_buscar_id(request, id):
#     noticia = Noticia.objects.get(pk=id)
#     data ={
#         'titulo': noticia.titulo,
#         'descripcion': noticia.descripcion,
#         'imagen': noticia.imagen
#     }
#     return JsonResponse(data)