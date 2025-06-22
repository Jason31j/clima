from django.db import models

# Create your models here.
class Weather(models.Model):
    dia = models.CharField(max_length=100)
    mes = models.IntegerField()
    agno = models.IntegerField()
    probabilidad = models.IntegerField()
    


    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.agno} => {self.probabilidad}%"
