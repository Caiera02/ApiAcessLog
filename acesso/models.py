from django.db import models

class LogAcesso(models.Model):

    matricula = models.IntegerField( verbose_name="Matrícula do Cooperado", db_index=True )
    nome = models.CharField(max_length=255,verbose_name="Nome Completo" )
    data_acesso = models.DateTimeField(auto_now_add=True,verbose_name="Data e Hora do Acesso" )

    class Meta:
        verbose_name = "Registro de Acesso"
        verbose_name_plural = "Registros de Acesso"
        ordering = ['-data_acesso'] # Ordena do mais recente para o mais antigo

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.data_acesso.strftime('%d-%m-%Y %H:%M')}"