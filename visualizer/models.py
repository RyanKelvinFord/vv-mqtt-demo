from django.db import models

class EnergyData(models.Model):
    country_code = models.CharField(max_length=10)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.country_code} - {self.value}"