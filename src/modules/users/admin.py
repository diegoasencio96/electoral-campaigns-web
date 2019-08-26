from django.contrib import admin
from .models import User
from django.contrib.auth import admin as auth_admin
from import_export.admin import ImportExportModelAdmin
from .forms import UserAddForm, UserEditForm

# Register your models here.


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'cellphone', 'identification_card')
    form = UserEditForm
    add_form = UserAddForm
    filter_horizontal = ('groups', )
    search_fields = ('username', 'first_name', 'last_name', 'identification_card',)
    list_filter = ('campaign',)
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined',)
    autocomplete_fields = ['campaign', 'country']
    fieldsets = (
        ('Información de acceso al sistema', {'fields': ('campaign', 'email', 'username', 'password', 're_password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'identification_card', 'cellphone', 'birth_date')}),
        ('Ubicación', {'fields': ('country',  'address',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',)}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    # actions = ()
