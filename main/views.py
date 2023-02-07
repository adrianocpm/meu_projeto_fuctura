from .serializers import ConcessionariaSerializer
from rest_framework import viewsets, permissions
from .models import Concessionaria

class ConcessionariaViewSet(viewsets.ModelViewSet):
    queryset = Concessionaria.objects.all()
    serializer_class= ConcessionariaSerializer
    permission_classes= [permissions.IsAuthenticated]

