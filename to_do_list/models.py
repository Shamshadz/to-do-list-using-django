from django.db import models

# Create your models here.
class Create(models.Model):
    title = models.CharField(max_length=1000)
    textarea = models.CharField(max_length=10000)

    def __str__(self):
        return self.title