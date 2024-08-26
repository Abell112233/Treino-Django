from django import forms
from .models import Aluno, Curso  

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'cpf' : forms.TextInput(attrs={'class':'form-control'}),
            'data_nascimento' : forms.DateInput(attrs={'class':'form-control'}),
            'foto' : forms.FileInput(attrs={'class':'form-control'}),
            'curso' : forms.SelectMultiple(attrs={'class':'form-control'}),
        }


class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'descricao' : forms.Textarea(attrs={'class':'form-control'}),
            'carga_horaria' : forms.TextInput(attrs={'class':'form-control'}),
        }