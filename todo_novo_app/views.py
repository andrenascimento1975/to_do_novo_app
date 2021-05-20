from .models import Tarefa, Grupos, Sub_Grupos
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class Logar(LoginView):
    template_name = 'login/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('grupos')


class Registrar(FormView):
    template_name = 'login/registrar.html'
    fields = '__all__'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tarefas')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registrar, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tarefas')
        return super(Registrar, self).get(*args, **kwargs)


class Sair(LogoutView):

    def get_success_url(self):
        return reverse_lazy('login')


class ListaTarefa(LoginRequiredMixin, ListView):
    model = Tarefa
    fields = '__all__'
    context_object_name = 'tarefas'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tarefas'] = data['tarefas'].filter(user=self.request.user)
        data['count'] = data['tarefas'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            data['tarefas'] = data['tarefas'].filter(
                title__startswith=search_input)
        data['search_input'] = search_input
        return data


class TodasTarefas(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name = 'completo'


class Criar(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/formulario.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Criar, self).form_valid(form)


class Atualizar(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/formulario.html'


class AtualizarGrupo(LoginRequiredMixin, UpdateView):
    model = Grupos
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/formulario_grupos.html'


class Apagar(DeleteView, LoginRequiredMixin):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
    template_name = 'login/confirmar.html'


class ApagarGrupo(LoginRequiredMixin, DeleteView):
    model = Grupos
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/apagar_grupo.html'


class CriarGrupo(LoginRequiredMixin, CreateView):
    model = Grupos
    context_object_name = 'criar_grupo'
    success_url = reverse_lazy('grupos')
    fields = '__all__'
    template_name = 'login/formulario_grupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarGrupo, self).form_valid(form)


class VisualizaGrupo(LoginRequiredMixin, ListView):
    model = Grupos
    fields = '__all__'
    context_object_name = 'criar_grupo'
    success_url = reverse_lazy('grupos')
    template_name = 'login/grupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VisualizaGrupo, self)


class MostraTarefaGrupo(LoginRequiredMixin, View):

    def get(self, request, pk):
        grupo_especifico = Grupos.objects.get(id=pk)
        join = grupo_especifico.tarefa_grupos.all()
        context = {'join': join}

        return render(request, "login/mostra_tarefa_grupo.html", context)


class VisualizaSubGrupo(LoginRequiredMixin, ListView):
    model = Sub_Grupos
    fields = '__all__'
    context_object_name = 'criar_subgrupo'
    success_url = reverse_lazy('subgrupos')
    template_name = 'login/subgrupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VisualizaSubGrupo, self)


class CriarSubGrupo(LoginRequiredMixin, CreateView):
    model = Sub_Grupos
    context_object_name = 'criar_subgrupo'
    success_url = reverse_lazy('subgrupos')
    fields = '__all__'
    template_name = 'login/formulario_subgrupos.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CriarSubGrupo, self).form_valid(form)



class AtualizarSubGrupo(LoginRequiredMixin, UpdateView):
    model = Sub_Grupos
    fields = '__all__'
    success_url = reverse_lazy('subgrupos')
    template_name = 'login/formulario_subgrupos.html'


class ApagarSubGrupo(LoginRequiredMixin, DeleteView):
    model = Sub_Grupos
    fields = '__all__'
    success_url = reverse_lazy('subgrupos')
    template_name = 'login/apagar_subgrupo.html'



class MostraSubGrupo(LoginRequiredMixin, View):

    def get(self, request, pk):
        grupo_especifico = Sub_Grupos.objects.get(id=pk)
        join_subgrupo = grupo_especifico.tarefa_grupos.all()
        context = {'join_subgrupo': join_subgrupo}
        return render(request, "login/mostra_subgrupo.html", context)

