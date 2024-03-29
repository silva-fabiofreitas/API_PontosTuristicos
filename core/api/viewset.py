from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from core.models import PontoTuristico, DocRG
from .serializers import PontoTuristicoSerializer, DocRGSerializer

'''
O viewset é uma view baseada em classe
'''

class DocRGViewSet(ModelViewSet):
    queryset = DocRG.objects.all()
    serializer_class = DocRGSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

class PontoTuristicoViewSet(ModelViewSet):
    '''
    queryset = PontoTuristico.objects.all(), uma vez sobreescrito o
    query set há a necessidade de definir um base name na router
    vc também pode criar seus proprios metodos personalizados usando action  
    '''      
    serializer_class = PontoTuristicoSerializer # Quais os campos serão incluidos no json
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ('^nome', 'descricao', 'endereco__linha1') 
    # lookup_field = ('nome') altera o id de busca na url, tem que ser unico

    def get_queryset(self):
        """
        Para realizar buscas na api pode ser passado uma query_string (parametros da url)
        e aqui realizado os filtros. Há formas mais faceis de realizar isso usando o pacote django-filter 
        """
        return PontoTuristico.objects.filter(aprovado=True)
    
    def list(self, request, *args, **kwargs):
        """
        Sobreescrendo o método, mantendo o mesmo comportamento com super da classe mãe
        """
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    @action(methods=['GET'], detail=True) # se detail true aponta pra um recurso senão para o endpoint
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['POST'], detail=True) 
    def associar_atracoes(self, request, pk):
        """
            Uma forma de criar um ponto com objeto aninhado uma vez que ele
        esteja declarado dentro da classe do Serializer
        """
        atracoes_id = request.data['ids']
        ponto = PontoTuristico.objects.get(id=pk)
        ponto.atracoes.set(atracoes_id)

        ponto.save()
        return HttpResponse('ok')
        
