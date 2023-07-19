from django.db import models

class Depoimento(models.Model):
    foto = models.ImageField(blank=True)
    depoimento = models.TextField(max_length=100)
    nome_pessoa = models.CharField(max_length=30)

    def __str__(self):
        return self.depoimento
    
