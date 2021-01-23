from django.db import models
from django.conf import settings

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

    title = models.CharField(max_length=64)
    content = models.TextField()
    author = models.CharField(max_length=24)

    #override str() to return title
    def __str__(self):
        return self.title

''' Comment class that is maped many to one post'''

class Comment(models.Model):

    content = models.TextField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now=True, verbose_name="Created At")
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['create']