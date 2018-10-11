from rest_framework import serializers
from pdb_store.models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', )

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('page', )


class LetterSerializer(serializers.ModelSerializer):
    letter_pages = PageSerializer(many=True)
    author = AuthorSerializer()
    class Meta:
        model = Letter
        fields = ('author', 'letter_pages')

