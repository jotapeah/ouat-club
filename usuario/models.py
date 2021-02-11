from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import UsuarioManager


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email',
                              max_length=200, blank=False, null=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    nome_completo = models.CharField(
        verbose_name='Nome completo', max_length=200, blank=False, null=False)


    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["nome_completo", ]

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
