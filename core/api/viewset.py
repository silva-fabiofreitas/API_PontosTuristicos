from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

'''
O viewset é uma view baseada em classe
'''


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()    
    serializer_class = PontoTuristicoSerializer # Quais os campos serão incluidos no json
