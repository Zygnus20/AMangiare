from django.contrib import admin
from productos.models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass
