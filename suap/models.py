from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome