from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100,verbose_name="Titulo")
    author = models.CharField(max_length=100,verbose_name="Autor")
    genre = models.CharField(max_length=20,verbose_name="Genero")
    karaoke = models.BooleanField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")
    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"
        ordering = ['-created_at']
    def __str__(self):
        return self.title

