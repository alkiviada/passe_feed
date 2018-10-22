from django.db.models import Max, Min

from rest_framework import viewsets
from rest_framework.response import Response

from pdb_store.serializers import FeedItemSerializer
from pdb_store.models import FeedItem

from random import randint





class FeedItemViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """

  queryset = FeedItem.objects.all()

  def list(self, request):
    queryset = FeedItem.objects.all()
    fi_min_pk = queryset.aggregate(Min('pk'))['pk__min']
    fi_max_pk = queryset.aggregate(Max('pk'))['pk__max']
    items = []
    while len(items) < 6:
      item = queryset.filter(pk=randint(fi_min_pk, fi_max_pk))
      if item:
        items.extend(item)
      
    serializer = FeedItemSerializer(items, many=True)
    print('I am returning some feeds')
    return Response(serializer.data)

  serializer_class = FeedItemSerializer

