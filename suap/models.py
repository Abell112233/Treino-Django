from django.db import models

# Create your models here.
    
class Curso(models.Model):
    nome = models.CharField(max_length=250)
    carga_horaria = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="curso/", null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to="curso/", null=True, blank=True)
    curso = models.ManyToManyField(Curso)
    def __str__(self):
        return (self.nome)