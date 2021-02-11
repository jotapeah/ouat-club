from django.contrib import admin
from .forms import UsuarioCreationForm, UsuarioChangeForm

from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario

    list_display = (
        "username",
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
        (None, {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ("nome_completo",)}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'is_superuser', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
        ('Contact info', {'fields': ("email",)}),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'), }),)

    search_fields = ("username", "nome_completo", "email",)
    ordering = ("nome_completo",)


admin.site.register(Usuario, UsuarioAdmin)
