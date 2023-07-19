from django.contrib import admin
from trips.models import Depoimento

class Depoimentos(admin.ModelAdmin):
    list_display = ('foto', 'depoimento', 'nome_pessoa')
    list_display_links = ('depoimento', 'nome_pessoa')
    search_fields = ('nome_pessoa',)
    list_per_page = 5

admin.site.register(Depoimento, Depoimentos)