from rest_framework import serializers
from pdb_store.models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', )

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('part', )


class FeedItemSerializer(serializers.ModelSerializer):
    item_parts = PartSerializer(many=True)
    class Meta:
        model = FeedItem
        fields = ('item_parts', )

