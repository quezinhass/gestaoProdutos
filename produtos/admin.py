from django.contrib import admin
from .models import Produto #Importa "Produto"

# Register your models here.
admin.site.register(Produto) # Permite que "produto" apareça na tela de administração do django