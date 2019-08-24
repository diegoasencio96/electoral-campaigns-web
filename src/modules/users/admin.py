from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from import_export.admin import ImportExportModelAdmin
# from .forms import UserAddForm, UserEditForm


# Register your models here.


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'cellphone', 'identification_card')
    # form = UserEditForm
    filter_horizontal = ('groups', )
    search_fields = ('username', 'first_name', 'last_name', 'identification_card',)
    list_filter = ('campaign',)
    # actions = ()
    '''
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return UserAddForm
        else:
            return super(UserAdmin, self).get_form(request, obj, **kwargs)
    '''
