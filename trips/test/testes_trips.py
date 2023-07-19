from rest_framework.test import APITestCase
from trips.models import Depoimento
from django.urls import reverse
from rest_framework import status

class DepoimentosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Depoimentos-list')
        self.depoimento_1 = Depoimento.objects.create(
            foto='' , depoimento='Depoimento teste 1 ', nome_pessoa='Teste da silva'
        )
        self.depoimento_2 = Depoimento.objects.create(
            foto='' , depoimento='Depoimento teste 2 ', nome_pessoa='Teste2 da silva'
        )
        
    # def test_falhador(self):
    #     self.fail('Teste falhou de proposito') 

    def test_requisicao_get_para_listar_depoimentos(self):
        """Teste para listar depoimentos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_depoimentos(self):
        """Teste para criar depoimentos"""
        data = {
            'foto':'',
            'depoimento':'Depoimento teste 3',
            'nome_pessoa':'Teste3 da silva'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_depoimento_(self):
        """Teste para atualizar depoimento"""
        data = {
            'foto':'',
            'depoimento':'Depoimento teste 1 atualizado',
            'nome_pessoa':'Teste da silva'
        }
        response = self.client.put('/depoimentos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_depoimento(self):
        """Teste para deletar depoimento"""
        response = self.client.delete('/depoimentos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)