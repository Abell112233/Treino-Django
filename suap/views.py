from django.shortcuts import render
from .models import Curso, Aluno

# Create your views here.

def index(request):
    cursos = Curso.objects.all()
    contexto = {
        'lista' : cursos
    }
    return render(request, 'suap/index.html', contexto)

def Informatica(request):
    alunos = Aluno.objects.filter(nome='Informática')
    contexto = {
        'lista2' : alunos
    }
    return render(request, 'suap/informatica.html', contexto)