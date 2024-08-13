from django.shortcuts import render
from .models import Aluno
# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    contexto = {
        'lista': alunos,
    }
    return render(request, 'suap/index.html', contexto)
    