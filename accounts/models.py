from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from config import settings


class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    username = models.CharField(max_length=50, unique=True, verbose_name='Usuario')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Correo electrónico')
    phone_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    # required
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='Última sesión')
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    is_active = models.BooleanField(default=False, verbose_name='Activo')
    is_superadmin = models.BooleanField(default=False, verbose_name='Super Admin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyUserManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    address_line_1 = models.CharField(max_length=100, blank=True, verbose_name='Direccion línea 1')
    address_line_2 = models.CharField(max_length=100, blank=True, verbose_name='Direccion línea 2')
    profile_picture = models.ImageField(upload_to='userprofile', verbose_name='Imágen de perfil')
    city = models.CharField(max_length=50, blank=True, verbose_name='Ciudad')
    state = models.CharField(max_length=50, blank=True, verbose_name='Estado/Región')
    country = models.CharField(max_length=50, blank=True, verbose_name='País')

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfil de usuarios'

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name