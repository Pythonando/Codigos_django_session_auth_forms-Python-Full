from django.contrib import admin
from .models import Users
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import admin as admin_auth_django

@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Informações residenciais', {'fields': ("rua", "numero", "cep")}),
    )
    readonly_fields = ('rua', 'numero', 'cep')
    

