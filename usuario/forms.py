from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Usuario
        fields = ("nome_completo", "email",)


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ("nome_completo", "email",)
