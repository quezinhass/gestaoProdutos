from django.db import models # importa o pacote model

# Create your models here.
class Produto(models.Model): #Todo model tem que herdar de models.Model
    nome = models.CharField(max_length=255) # Todo CharField tem que ter o tamanho máximo 
    preco = models.DecimalField(max_digits=7, decimal_places=2) # Todo DecimalField tem que ter o max_digits e o decimal_places
    tipo = models.CharField(max_length=255)
    descricao = models.TextField() # O TextField não precisa necessariamente passar parâmetros

    # Equivale ao toString
    def __str__(self):
        return str(self.nome)
