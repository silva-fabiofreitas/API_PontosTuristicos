from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

'''
O viewset é uma view baseada em classe
'''


class PontoTuristicoViewSet(ModelViewSet):
    '''
    queryset = PontoTuristico.objects.all(), uma vez sobreescrito o
    query set há a necessidade de definir um base name na router
    vc também pode criar seus proprios metodos personalizados usando action  
    '''
      
    serializer_class = PontoTuristicoSerializer # Quais os campos serão incluidos no json

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['GET'], detail=True) # se detail true aponta pra um recurso senão para o endpoint
    def denunciar(self, request, pk=None):
        pass