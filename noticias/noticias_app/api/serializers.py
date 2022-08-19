from rest_framework import serializers
from noticias_app.models import Categoria, Noticia

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields ="__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    noticialist = NoticiaSerializer(many=True, read_only=True)
    # noticialist = serializers.StringRelatedField(many=True) # llama al metodo str del modelo
    class Meta:
        model = Categoria
        fields = "__all__"


        




# class NoticiaSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     titulo = serializers.CharField()
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
    
#     def create(self, validadorDatos):
#         return Noticia.objects.create(**validadorDatos)
    
#     def update(self, instancia, validadorDatos):
#         instancia.titulo = validadorDatos.get('titulo',instancia.titulo)
#         instancia.descripcion = validadorDatos.get('descripcion',instancia.descripcion)
#         instancia.imagen = validadorDatos.get('imagen',instancia.imagen)
#         instancia.save()
#         return instancia
        