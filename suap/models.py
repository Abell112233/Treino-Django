from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    matricula = models.CharField(max_length=50)
    
    def __str__(self):
        return (self.nome + ' - ' + self.matricula)
    
class Curso(models.Model):
    nome = models.CharField(max_length=250)
    carga_horaria = models.CharField(max_length=50)
    descricao = models.TextField()
    alunos = models.ManyToManyField(Aluno)
    
    def __str__(self):
        return self.nome
    