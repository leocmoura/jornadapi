from django.contrib import admin
from trips.models import Depoimento, Destino

class Depoimentos(admin.ModelAdmin):
    list_display = ('foto', 'depoimento', 'nome_pessoa')
    list_display_links = ('depoimento', 'nome_pessoa')
    search_fields = ('nome_pessoa',)
    list_per_page = 5

admin.site.register(Depoimento, Depoimentos)

class Destinos(admin.ModelAdmin):
    list_display = ('foto', 'nome_destino', 'preco')
    list_display_links = ('foto', 'nome_destino', 'preco')
    search_fields = ('nome_destino',)
    list_per_page = 5

admin.site.register(Destino, Destinos)