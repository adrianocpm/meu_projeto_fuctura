from django.db import models
import uuid

class Concessionaria (models.Model):
    SETOR_CHOICE = [
        ('oficina', 'Oficina'),
        ('showroon', 'Showroon'),
        ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank =True)
    
    codigo = models.CharField(
        max_length=8,
        null=False, 
        blank=False)
    
    setor = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=SETOR_CHOICE)
    
    veiculo = models.TextField(
        null=False,
        blank=False,
        max_length=20)
        
    
    quantidade_veiculos = models.IntegerField(
        null=False,
        blank=False,
        max_length=5)
      
    

    


