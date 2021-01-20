from django.db import models

# Create your models here.

""" This TimeCheckModel checks when record was last modified and created """
class TimeCheckModel(models.Model):
    update = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Created At",)

    #an abstract class, It cannot be used as a normal Django model, but has to be inherited
    class Meta:
        abstract = True

''' Post class that inherits TimeCheckModel properties'''
class Post(TimeCheckModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    #used to add html markdown to description
    description_markdown = models.TextField(blank=True)
    author = models.CharField(max_length=250)

    #override str() to return title
    def __str__(self):
        return self.title