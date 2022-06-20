from django.db import models
from django.contrib.auth.models import User


class Catalogo(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    posted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titile
