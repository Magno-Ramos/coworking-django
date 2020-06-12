from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Agendamento


# Create your views here.
class AgendamentosList(ListView):
    model = Agendamento
    template_name = 'agendamentos/agendamentos.html'


class AgendamentosDetail(DetailView):
    model = Agendamento
    template_name = 'agendamentos/agendamento_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AgendamentoCreate(CreateView):
    model = Agendamento
    fields = ['solicitante', 'horario_inicio', 'horario_termino', 'status', 'salas']
    success_url = reverse_lazy('agendamentos')


class AgendamentoUpdate(UpdateView):
    model = Agendamento
    fields = ['solicitante', 'horario_inicio', 'horario_termino', 'status', 'salas']
    success_url = reverse_lazy('agendamentos')


class AgendamentoDelete(DeleteView):
    model = Agendamento
    success_url = reverse_lazy('agendamentos')
