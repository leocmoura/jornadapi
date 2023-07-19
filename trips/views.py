from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from trips.models import Depoimento
from trips.serializer import DepoimentoSerializer 

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
