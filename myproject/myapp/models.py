from django.db import models


class Model1(models.Model):
    field1 = models.CharField(max_length=50)
class Model2(models.Model):
    field = models.CharField(max_length=50)
class Model3(models.Model):
    field1 = models.CharField(max_length=50)
class Model4(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField(default=0)