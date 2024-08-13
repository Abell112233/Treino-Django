from django.db import models

# Create your models here.
    
class Curso(models.Model):
    nome = models.CharField(max_length=250)
    carga_horaria = models.CharField(max_length=50)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    matricula = models.CharField(max_length=50)
    curso = models.ManyToManyField(Curso)
    def __str__(self):
        return (self.nome + ' - ' + self.matricula)