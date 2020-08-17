from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

""""
:Posibilidad de crear mi usuario empleado basado en los modelos user

"""


class EmpleadoManager(BaseUserManager):

    def create_user(self, email, username, nombre, apellido, password=None):
        if not email:
            raise ValueError('El usuario debe tener un  correo electronico')
        usuario = self.model(username=username, email=self.normalize_email(
            email), nombre=nombre, apellido=apellido)
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, nombre, apellido, password):
        usuario = self.create_user(
            email, username=username, nombre=nombre, apellido=apellido, password=password)
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Empleado(AbstractBaseUser):
    username = models.CharField(
        'nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('correo', unique=True, max_length=240)
    nombre = models.CharField(max_length=240, blank=True, null=True)
    apellido = models.CharField(max_length=240, blank=True, null=True)
    imagen = models.ImageField('foto de perfil', upload_to='perfil/',
                               height_field=None, width_field=None, max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = EmpleadoManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    def __str__(self):
        return "usuario : {}".format(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
