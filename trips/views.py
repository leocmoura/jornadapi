from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from trips.models import Depoimento, Destino
from trips.serializer import DepoimentoSerializer, DestinoSerializer

import random 

class DepoimentosViewSet(viewsets.ModelViewSet):
    """Exibindo depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer

class DepoimentosHomeViewSet(viewsets.ModelViewSet):
    """Exibindo 3 depoimentos de forma randomica"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer
    allowed_methods = ['GET']
    
    def list(self, request):
        random_depoimentos = random.sample(list(self.queryset), 3)
        serializer_class = DepoimentoSerializer(random_depoimentos, many=True)
        return Response(serializer_class.data)

class DestinosViewSet(viewsets.ModelViewSet):
    """Exibindo destinos"""
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome_destino']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"message": "Nenhum destino encontrado."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    