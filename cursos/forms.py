from datetime import date
from django import forms

from cursos.models import Curso

class CursoForm(forms.ModelForm):
    def clean_data_do_curso(self):
        data_do_curso = self.cleaned_data['data_do_curso']
        hoje = date.today()
        if data_do_curso < hoje:
            raise forms.ValidationError('Não é possível cadastrar um curso com data retroativa')
        return data_do_curso
    class Meta:
        model = Curso
        fields = ['titulo', 'nivel', 'carga_horaria', 'data_do_curso', 'descricao']




