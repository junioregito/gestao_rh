from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao','arquivo']


    #override no post para adicinar um objeto de instância
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # Recebi de outra tela essa informação
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

#    def form_valid(self, form):
##        obj = form.save()
#        funcionario = self.request.user.funcionario
#        funcionario.empresa = obj
#        funcionario.empresa = self.request.user.funcionario.empresa
#        funcionario.save()
#        return HttpResponse('Ok')

