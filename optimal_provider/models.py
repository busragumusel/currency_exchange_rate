from django.db import models


class Provider(models.Model):
    url = models.CharField(max_length=30)


class Currencies(models.Model):
    provider = models.CharField(max_length=20, default='')
    code = models.CharField(max_length=3, default='usd')
    rate = models.FloatField(default=0)
