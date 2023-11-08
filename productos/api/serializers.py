from rest_framework import serializers
from productos.models import Producto
from categorias.api.serializers import CategoriaSerializer

class ProductoSerializer(serializers.ModelSerializer):
    categoria_data = CategoriaSerializer(source="categoria", read_only=True)
    class Meta:
        model = Producto
        fields = ['id','title','image','descripcion','precio','active','categoria','categoria_data']