from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreationForm, UsuarioChangeForm

from .models import Usuario


class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario

    list_display = (
        "email",
        "nome_completo",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ("nome_completo",)}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'is_superuser', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome_completo', 'password1', 'password2'), }),)

    search_fields = ("nome_completo", "email",)
    ordering = ("nome_completo",)


admin.site.register(Usuario, UsuarioAdmin)
