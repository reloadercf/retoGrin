from django.db import models


choice_status=(
    ('Created','Created'),
    ('Maintenance','Maintenance'),
    ('Distributing','Distributing'),
    ('OnStreet','OnStreet'),
)

class Scooter(models.Model):
    serie=models.CharField(max_length=50)
    modelo=models.IntegerField(blank=True,null=True)
    descripcion=models.TextField(blank=True, null=True)
    status=models.CharField(choices=choice_status, max_length=50,default='Created')
    fechaultimostatus=models.DateTimeField(auto_now=True)
    fechacreacion=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.serie

class Historial(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=choice_status, max_length=50,default='Created')
    scooter=models.ForeignKey(Scooter, related_name="moviliario" , on_delete=models.CASCADE)
    def __str__(self):
        return self.scooter.serie