from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from atracoes.api.serializers import AtracoesSerializer

from atracoes.models import Atracoes

class AtracoesViewSet(ModelViewSet):
    queryset = Atracoes.objects.all()
    serializer_class = AtracoesSerializer
    """
    Usando o django-filter, adicionar no settings ou importa para cada viewset
    """
    filter_backends = [DjangoFilterBackend] # Já importado no settings
    # Também aceita um dicionario
    filterset_fields = {
        'nome': ['contains'], 
        'descricao': ['contains'],
        'idade_minima': ['gte', 'lte']} 
    # filterset_fields = ('nome', 'descricao', 'idade_minima')