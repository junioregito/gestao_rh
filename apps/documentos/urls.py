from django.urls import path
from .views import DocumentoCreate

urlpatterns = [
    # enviado o funcinario_id para outra tela
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
#    path('deletar/<int:pk>/', EmpresaCreate.as_view(), name='edit empresa'),
]