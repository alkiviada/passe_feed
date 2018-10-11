from django.db.models import Max, Min

from rest_framework import viewsets
from rest_framework.response import Response

from pdb_store.serializers import LetterSerializer
from pdb_store.models import Letter

from pdb_store.helpers import get_random_pks





class LetterViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """

  queryset = Letter.objects.all()

  def list(self, request):
    queryset = Letter.objects.all()
    letter_min_pk = queryset.aggregate(Min('pk'))['pk__min']
    letter_max_pk = queryset.aggregate(Max('pk'))['pk__max']
    queryset = queryset.filter(pk__in=get_random_pks(5, [letter_min_pk, letter_max_pk]))
    serializer = LetterSerializer(queryset, many=True)
    return Response(serializer.data)

  serializer_class = LetterSerializer

