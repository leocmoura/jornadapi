import os

from rest_framework import serializers
from trips.models import Depoimento, Destino
from trips.validators import descricao_valida

from dotenv import load_dotenv
from bardapi import Bard

class DepoimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimento
        fields = '__all__'

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'
        # exclude = ('id',)

    def validate(self, data):
        if descricao_valida(data['descricao']):
            load_dotenv()

            token = os.getenv('_BARD_API_KEY')
            bard = Bard(token=token)

            # prompt = f"Faça um resumo sobre {data['nome_destino']} enfatizando o porque este lugar é incrível. Utilize uma linguagem informal e até 100 caracteres no máximo em cada parágrafo. Crie 2 parágrafos neste resumo sem quebras de linhas."
            prompt = f"Faça um pequeno texto de descrição para {data['nome_destino']} em 2 parágrafos. Limite de 100 caracteres em cada parágrafo. Utilize linguagem informal. Não inclua a sua introdução de resposta e nem a conclusão. Não utilize tópicos ou listas."
            response = bard.get_answer(prompt)['content']
            
            data['descricao'] = response
        
        return data