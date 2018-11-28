from django.db import models

# Create your models here.

class CryptoBalance(models.Model):
    balanceBTC = models.IntegerField(default=0)
    balanceLTC = models.IntegerField(default=0)
    balanceXRP = models.IntegerField(default=0)
    balanceETH = models.IntegerField(default=0)
    balanceXLM = models.IntegerField(default=0)
    balanceXMR = models.IntegerField(default=0)
    balanceADA = models.IntegerField(default=0)
    balanceTRX = models.IntegerField(default=0)
    balanceEOS = models.IntegerField(default=0)
    balanceBCH = models.IntegerField(default=0)

    def __str__(self):
        return self.id
