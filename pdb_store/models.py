from django.db import models

# Create your models here.

class Letter(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='author_letters', null=True)
    def __str__(self):
      return str(self.pk)

    def __unicode__(self):
      return self.pk
    
    class Meta:
      ordering = ('pk',)

class Page(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='letter_pages', null=True)
    page = models.TextField()
    def __str__(self):
        return self.page
    class Meta:
        ordering = ('pk',)

class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name
