from django.contrib import admin
from acesso.models import LogAcesso

@admin.register(LogAcesso)
class LogAcessoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'data_acesso')
    list_filter = ('data_acesso',)
    search_fields = ('nome', 'matricula')

# Crie um superusuário no terminal (python manage.py createsuperuser)
# e acesse o /admin do seu site para ver os logs salvos.