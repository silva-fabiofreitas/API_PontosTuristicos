from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer 
from enderecos.api.serializers import EnderecoSerializer 

class PontoTuristicoSerializer(ModelSerializer):
    '''
        É uma boa pratica listar somente alguns campos, quando selecionar o recurso
    que é exibido ele completo. Se incluir tudo fica muito pesado para um celular
    ou aplicação exibir.
        SerializerMethodField() # Personaliza o retorno, gera um campo adicional.
    O ideal é que a regra de negocio fique nos managers ou models

    '''
    atracoes = AtracoesSerializer(many=True) # Serializa objetos aninhados
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
       
        fields = (
            'id', 'nome', 'descricao', 'aprovado','foto',
            'atracoes','comentarios' ,'avaliacoes', 'endereco',
            'descricao_completa', 'descricao_completa2'
        ) 

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'