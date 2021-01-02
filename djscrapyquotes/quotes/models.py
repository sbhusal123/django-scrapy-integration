from django.db import models

class Quotes(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField(unique=True)

    def __str__(self):
        return self.text
