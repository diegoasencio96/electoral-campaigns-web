from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.contrib.auth.models import Group

PASSWORD_LEN = 6


class UserAddForm(forms.ModelForm):
    re_password = forms.CharField(label=_('Confirmar contraseña'), widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = (
            'campaign', 'username', 'password', 're_password', 'first_name', 'last_name', 'identification_card',
            'email', 'country', 'address', 'cellphone', 'birth_date', 'is_staff', 'is_active',
            'is_superuser', 'groups',)
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password is not None:
            password = password.strip()
            if len(password) >= PASSWORD_LEN:
                return make_password(password)
            else:
                raise forms.ValidationError(str(_('passwords must have {} or more characters')).format(PASSWORD_LEN))
        else:
            raise forms.ValidationError(_('enter a valid password'))

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        if password is not None:
            re_password = self.cleaned_data.get('re_password').strip()
            if check_password(re_password, password):
                return re_password
            else:
                raise forms.ValidationError(_('passwords do not match'))
        else:
            raise forms.ValidationError(_('enter a valid password'))


class UserEditForm(forms.ModelForm):
    now_password = forms.CharField(label=_('Contraseña actual'), widget=forms.PasswordInput(render_value=True),
                                   required=False)
    password = forms.CharField(label=_('Nueva contraseña'), widget=forms.PasswordInput(), required=False)
    re_password = forms.CharField(label=_('Confirme la nueva contraseña'), widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = (
            'campaign', 'username', 'password', 're_password', 'first_name', 'last_name', 'identification_card',
            'email', 'country', 'address', 'cellphone', 'birth_date', 'is_staff', 'is_active',
            'is_superuser', 'groups',)

    def clean(self):
        cleaned_data = super(UserEditForm, self).clean()
        now_password = cleaned_data.get("now_password")
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if now_password == "" and password == "" and re_password == "":
            cleaned_data['password'] = self.instance.password
        elif now_password != "" and password != "" and re_password != "":
            pass
        else:
            raise forms.ValidationError(_('Enter the required fields'))

    def clean_now_password(self, *args, **kwargs):
        now_password = self.cleaned_data.get('now_password')
        if self.instance.check_password(now_password) or now_password == "":
            return now_password.strip()
        else:
            raise forms.ValidationError(_('incorrect password'))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password is not None:
            password = password.strip()
            if len(password) >= PASSWORD_LEN or password == "":
                password = '' if password == '' else make_password(password)
                return password
            else:
                raise forms.ValidationError(str(_('passwords must have {} or more characters')).format(PASSWORD_LEN))
        else:
            raise forms.ValidationError(str(_('passwords must have {} or more characters')).format(PASSWORD_LEN))

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        if password is not None:
            re_password = self.cleaned_data.get('re_password').strip()
            if check_password(re_password, password) or re_password == "":
                return re_password
            else:
                raise forms.ValidationError(_('passwords do not match'))
        else:
            raise forms.ValidationError(_('enter a valid password'))
