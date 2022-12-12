from django.forms import *
from .models import User


class RegistrationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Tus nombres'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Tus apellidos'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Tu número de teléfono'
        self.fields['email'].widget.attrs['placeholder'] = 'Tu correo electrónico'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Las contraseñas no coinciden')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        widgets = {
            'phone_number': TextInput(
                attrs={
                    'type': 'tel',
                }
            ),
        }

    password = CharField(
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tu contraseña',
            }
        )
    )

    confirm_password = CharField(
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirma tu contraseña',
            }
        )
    )