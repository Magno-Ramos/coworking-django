from django.urls import path
from agendamentos.views import AgendamentosList, AgendamentosDetail, AgendamentoCreate, AgendamentoUpdate, AgendamentoDelete

urlpatterns = [
    path('', AgendamentosList.as_view(), name='agendamentos'),
    path('create/', AgendamentoCreate.as_view(), name='agendamento_create_cbv'),
    path('update/<int:pk>', AgendamentoUpdate.as_view(), name='agendamento_update_cbv'),
    path('delete/<int:pk>', AgendamentoDelete.as_view(), name='agendamento_delete_cbv'),
    path('<int:pk>/', AgendamentosDetail.as_view(), name='agendamentos_detail_cbv'),
]
