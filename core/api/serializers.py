from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework.fields import SerializerMethodField
from atracoes.models import Atracoes
from core.models import DocRG, PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class DocRGSerializer(ModelSerializer):
    class Meta:
        model = DocRG
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    '''
        É uma boa pratica listar somente alguns campos, quando selecionar o recurso
    que é exibido ele completo. Se incluir tudo fica muito pesado para um celular
    ou aplicação exibir.
        SerializerMethodField() # Personaliza o retorno, gera um campo adicional.
    O ideal é que a regra de negocio fique nos managers ou models.
    endereco = SlugRelatedField(slug_field='cidade', read_only=True) ira retorna
    um atriburo do modelo selecionado ao inves do id 

        def create() precisa ser declarado para cria objetos com relações aninhadas

        EnderecoSerializer(read_only=True) # O campo não é mais obrigatorio na API, no entanto não salva

        Para criar um ponto turistico atribuindo um campo aninhado já existente, esse já declarado como atrações
    pode ser desenvolvida uma action personalizad.a 
    '''
    atracoes = AtracoesSerializer(many=True)  # Serializa objetos aninhados
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_rg = DocRGSerializer() # Relação one to one

    class Meta:
        model = PontoTuristico

        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto',
            'atracoes', 'comentarios', 'avaliacoes', 'endereco',
            'descricao_completa', 'descricao_completa2', 'doc_rg'
        )

        read_only_fields = ('comentarios', )

    def criar_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            obj_atracoe = Atracoes.objects.create(**atracao)
            ponto.atracoes.add(obj_atracoe)

    def create(self, validated_data):
        # Ao deletar consigo criar o ponto turistico da maneira abaixo
        atracoes = validated_data.pop('atracoes')
        endereco = validated_data.pop('endereco')
        doc = validated_data.pop('doc_rg')
        avaliacoes = validated_data.pop('avaliacoes')

        ponto = PontoTuristico.objects.create(**validated_data)
        self.criar_atracoes(atracoes, ponto)

        obj_endereco = Endereco.objects.create(**endereco)
        obj_doc = DocRG.objects.create(**doc)

        ponto.endereco = obj_endereco
        ponto.doc_rg = obj_doc
        ponto.avaliacoes.set(avaliacoes)

        return ponto

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'
