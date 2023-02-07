from rest_framework import serializers
from .models import Concessionaria

class ConcessionariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionaria
        fields = [
            'id',
            'codigo',
            'setor',
            'veiculo',
            'quantidade_veiculos'
        ]
