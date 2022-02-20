from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        '''
        É uma boa pratica listar somente alguns campos, quando selecionar o recurso
        que é exibido ele completo. Se incluir tudo fica muito pesado para um celular
        ou aplicação exibir 
        '''
        fields = ('id', 'nome', 'descricao') 
