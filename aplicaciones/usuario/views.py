from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import FormularioLogin, ModelUsuarioForm
from .models import Empleado
# Create your views here.

# Creamos la vista de clase para el login al sistema


class LoginView(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    # Metodo para decirle al Django que me inicie la sesion

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


# cierre de sesion


def cerrar_sesion(request):
    logout_url = reverse_lazy('login')
    logout(request)
    return HttpResponseRedirect(logout_url)


class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = ModelUsuarioForm
    template_name = "registro.html"
    success_url = reverse_lazy('login')
