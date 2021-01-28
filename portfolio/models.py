from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length = 60,default="")
    contact_id = models.CharField(max_length=60,default="")
    message = models.TextField(default="")
    def __str__(self):
        return self.name