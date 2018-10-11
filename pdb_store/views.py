from rest_framework import viewsets
from pdb_store.serializers import LetterSerializer
from pdb_store.models import Letter


class LetterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

