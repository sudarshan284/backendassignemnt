from django.db import models
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default = 1)
    salary = models.IntegerField(default = 0)
