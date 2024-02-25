from django.contrib import admin

from base.models import Cadastro

# Register your models here.
#registra as tabelas que o admin tem acesso
#registra o modelo com qual model quer que apareça no banco de dados
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']
