from django.db import models


class Currencies(models.Model):
    provider = models.TextField(default='')
    code = models.CharField(max_length=3, default='usd')
    rate = models.FloatField(default=0)
