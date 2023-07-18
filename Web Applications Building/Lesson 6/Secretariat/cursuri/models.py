from django.db import models

# Create your models here.


class Course(models.Model):
    nume        = models.CharField(max_length=40)
    descriere   = models.TextField()
    dificultate = models.IntegerField()
    pret        = models.IntegerField()
    public      = models.BooleanField()

    def __str__(self):
        return self.nume