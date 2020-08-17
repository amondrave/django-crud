from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Empleado


class FormularioLogin(AuthenticationForm):
    # Inicializo la clase con los campos del formulario
    def __init__(self, *args, **kwargs):
        # llamo a la super clase para generar la instancia
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class ModelUsuarioForm(forms.ModelForm):
    """
    Definicion de elementos del formulario del empleado

    Variables 
        - password1: contrasena
        - password2: verificacion de contrasena
    """
    password1 = forms.CharField(label="contrasena", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'digite su contrasena',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label="contrasena de verificacion", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'vuelva y digite su contrasena',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Empleado
        fields = ['email', 'username', 'nombre', 'apellido']
        labels = {
            'email': 'Correo electronico',
            'username': 'Nombre de Usuario',
            'nombre': 'Digite su nombre',
            'apellido': 'Digite su apellido'
        }
        widget = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'correo electronico',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nombre de usuario',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'apellido'
                }
            )
        }
    # ahora tenemos que validar la contrasena para que esta se quede guardada

    def clean_password2(self):
        """
        Validamos la contraseña numero 2 para ver que ambas contraseñas
        sean iguales antes de que estas sean encriptadas y se envien a la base de datos, retorna la contraseña valida

        Exception:
          ValidationError -> arroja error si las contraseñas no son iguales
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

    # Sobreescribimos el metodo save para poder guardar el usuario con la contraseña
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
