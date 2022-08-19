from rest_framework.response import Response
from noticias_app.models import Noticia, Categoria
from noticias_app.api.serializers import NoticiaSerializer, CategoriaSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def noticia_listado(request):
    if request.method == 'GET':
        noticias = Noticia.objects.all()
        serializer = NoticiaSerializer(noticias, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        deserializer = NoticiaSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
            return Response(deserializer.errors)

@api_view(['GET','PUT','DELETE'])
def noticia_buscar_id(request, id):
    if(request.method =='GET'):
        noticia = Noticia.objects.get(pk=id)
        serializer = NoticiaSerializer(noticia)    
        return Response(serializer.data)
    
    if(request.method =='PUT'):
        noticia = Noticia.objects.get(pk=id)
        deserializer = NoticiaSerializer(noticia, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
            return Response(deserializer.errors)
    
    if request.method == 'DELETE':
        noticia = Noticia.objects.get(pk=id)
        noticia.delete()
        data={
            "resultado": True
        }
        return Response(data)
            
#CATEGORIAS

@api_view(['GET','POST'])
def categoria_listado(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        deserializer = CategoriaSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
            return Response(deserializer.errors)

@api_view(['GET','PUT','DELETE'])
def categoria_buscar_id(request, id):
    if(request.method =='GET'):
        categoria = Categoria.objects.get(pk=id)
        serializer = CategoriaSerializer(categoria)    
        return Response(serializer.data)
    
    if(request.method =='PUT'):
        categoria = Categoria.objects.get(pk=id)
        deserializer = CategoriaSerializer(categoria, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
            return Response(deserializer.errors)
    
    if request.method == 'DELETE':
        categoria = Categoria.objects.get(pk=id)
        categoria.delete()
        data={
            "resultado": True
        }
        return Response(data)