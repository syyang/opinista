from django.db import models

class Post(models.Model):
    message = models.CharField(max_length=1400)
    version = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

