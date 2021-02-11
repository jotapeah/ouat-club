from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import UsuarioManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='Usuário', max_length=50, blank=False, null=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    nome_completo = models.CharField(
        verbose_name='Nome completo', max_length=200, blank=False, null=False)
    email = models.EmailField(verbose_name='Email',
                              max_length=200, blank=False, null=False, unique=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["nome_completo", "password", ]

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
