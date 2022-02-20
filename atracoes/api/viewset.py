from rest_framework.viewsets import ModelViewSet
from atracoes.api.serializers import AtracoesSerializer

from atracoes.models import Atracoes

class AtracoesViewSet(ModelViewSet):
    queryset = Atracoes.objects.all()
    serializer_class = AtracoesSerializer