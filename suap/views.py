from django.shortcuts import render
from .models import Curso, Aluno
from .forms import AlunoForm, CursoForm

# Create your views here.

def index(request):
    cursos = Curso.objects.all()
    contexto = {
        'lista' : cursos
    }
    return render(request, 'suap/index.html', contexto)

def Informatica(request):
    alunos = Aluno.objects.filter(curso=1)
    contexto = {
        'lista2' : alunos
    }
    return render(request, 'suap/informatica.html', contexto)

def Alimentos(request):
    alunos = Aluno.objects.filter(curso=2)
    contexto = {
        'lista3' : alunos
    }
    return render(request, 'suap/alimentos.html', contexto)

def Apicultura(request):
    alunos = Aluno.objects.filter(curso=3)
    contexto = {
        'lista4' : alunos
    }
    return render(request, 'suap/apicultura.html', contexto)

def ADS(request):
    alunos = Aluno.objects.filter(curso=4)
    contexto = {
        'lista5' : alunos
    }
    return render(request, 'suap/ADS.html', contexto)
def Detalhe(request, aluno_id):
    detalhes = Aluno.objects.get(id=aluno_id)
    contexto = {
        'detalhes' : detalhes   
    }
    return render(request, 'suap/detalhes_aluno.html', contexto)

def Cadastro(request):
    formA = AlunoForm()
    fromC = CursoForm()
    contexto = {
        'formA' : formA,
        'fromC' : fromC
    }
    return render(request, 'suap/cadastro.html', contexto)