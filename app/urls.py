from django.contrib import admin
from django.urls import path, include 
from acesso.views import log_acesso_view
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as rotas do seu novo app:
    path('api/log_acesso/', log_acesso_view, name='log_acesso'), 
    # path('', include('log_app.urls')),
]