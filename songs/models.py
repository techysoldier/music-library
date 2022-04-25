from django.db import models

class Songs (models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.DecimalField(max_digits=8, decimal_places=2)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
   

   