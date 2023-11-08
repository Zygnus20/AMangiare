from django.contrib import admin
from categorias.models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
