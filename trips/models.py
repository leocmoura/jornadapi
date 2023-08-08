from django.db import models

class Depoimento(models.Model):
    '''Modelo de depoimentos'''
    def upload_foto_depoimento(instance, filename):
        type_file = filename.split(".")[-1]
        filename = instance.nome_pessoa.replace(" ", "_") + "." + type_file
        return f'depoimentos/{filename}'

    foto = models.ImageField(upload_to=upload_foto_depoimento, blank=True)
    depoimento = models.TextField(max_length=100)
    nome_pessoa = models.CharField(max_length=30)

    def __str__(self):
        return self.depoimento
    
class Destino(models.Model):
    def upload_foto_destino_1(instance, filename):
        type_file = filename.split(".")[-1]
        filename = instance.nome_destino.replace(" ", "_") + "1." + type_file
        return f'depoimentos/{filename}'

    def upload_foto_destino_2(instance, filename):
        type_file = filename.split(".")[-1]
        filename = instance.nome_destino.replace(" ", "_") + "2." + type_file
        return f'depoimentos/{filename}'

    foto_1 = models.ImageField(upload_to=upload_foto_destino_1, blank=True, null=True)
    foto_2 = models.ImageField(upload_to=upload_foto_destino_2, blank=True, null=True)
    nome_destino = models.CharField(max_length=30, blank=False, null=False)
    meta = models.CharField(max_length=160, default=None, null=False)
    descricao = models.TextField(max_length=200, blank=True, default=None, null=None)
    preco = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.nome_destino