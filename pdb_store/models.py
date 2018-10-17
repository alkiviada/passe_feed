from django.db import models

# Create your models here.

class FeedItem(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='author_items', null=True)
    def __str__(self):
      return str(self.pk)

    def __unicode__(self):
      return self.pk
    
    class Meta:
      ordering = ('pk',)

class Part(models.Model):
    feed_item = models.ForeignKey(FeedItem, on_delete=models.CASCADE, related_name='item_parts', null=True)
    part = models.TextField()
    def __str__(self):
        return self.part
    class Meta:
        ordering = ('pk',)

class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name
