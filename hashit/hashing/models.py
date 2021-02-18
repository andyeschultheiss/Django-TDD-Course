from django.db import models

class Hash(models.Model):
    text = models.TextField()
    hash_text = models.CharField(max_length=64)