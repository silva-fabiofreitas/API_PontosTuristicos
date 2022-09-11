from django.db import models

from atracoes.models import Atracoes
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from enderecos.models import Endereco

class DocRG(models.Model):
    descrição = models.CharField(max_length=20)

    def __str__(self):
        return self.descrição


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', blank=True, null=True) # instalar a biblioteca pilow para lidar com imagens   
    doc_rg = models.OneToOneField(DocRG, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def descricao_completa2(self):
        return f'{self.nome} - {self.descricao}'

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['-id']


    