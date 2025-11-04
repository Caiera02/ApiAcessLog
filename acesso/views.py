import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from acesso.models import LogAcesso 

# IMPORTANTE: Mantenha o @csrf_exempt ou implemente o token CSRF corretamente
@csrf_exempt 
def log_acesso_view(request):
    
    if request.method != 'POST':
        return JsonResponse({'message': 'Método não permitido.'}, status=405)

    try:
        data = json.loads(request.body)

        matricula = data.get('matricula')
        nome = data.get('nome')
        # data_acesso não é mais necessário, pois auto_now_add=True cuida disso

        if not all([matricula, nome]):
             # A validação é simplificada
            return JsonResponse({'message': 'Dados incompletos fornecidos.'}, status=400)
        
        # 1. SALVA OS DADOS NO BANCO DE DADOS
        LogAcesso.objects.create(
            matricula=matricula,
            nome=nome
            # data_acesso será preenchido automaticamente
        )

        return JsonResponse({'message': 'Log de acesso registrado com sucesso!'}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'message': 'Formato JSON inválido.'}, status=400)
    except Exception as e:
        return JsonResponse({'message': f'Erro interno do servidor: {str(e)}'}, status=500)