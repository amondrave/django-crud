from django.contrib.auth.forms import AuthenticationForm


class FormularioLogin(AuthenticationForm):
    # Inicializo la clase con los campos del formulario
    def __init__(self, *args, **kwargs):
        # llamo a la super clase para generar la instancia
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
