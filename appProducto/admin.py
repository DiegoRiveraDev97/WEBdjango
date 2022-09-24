from django.contrib import admin

# Register your models here.
from .models import Carrito, Producto

# Register your models here.
admin.site.register(Producto)
admin.site.register(Carrito)