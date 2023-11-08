from django.db import models

class Producto(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='productos')
    descripcion = models.CharField(max_length=255)
    precio = models.IntegerField()
    active = models.BooleanField(default=False)
    categoria = models.ForeignKey('categorias.Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title