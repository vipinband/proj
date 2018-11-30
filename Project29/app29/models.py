from django.db import models


class Feebback(models.Model):
    name = models.CharField(max_length=50)
    cno = models.IntegerField(default=10)
    message = models.CharField(max_length=500)


