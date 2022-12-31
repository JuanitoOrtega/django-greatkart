from django.forms import *
from .models import User, UserProfile


class RegistrationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Tus nombres'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Tus apellidos'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Tu número de teléfono'
        self.fields['email'].widget.attrs['placeholder'] = 'Tu correo electrónico'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

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


class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']
        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'phone_number': TextInput(
                attrs={
                    'type': 'tel',
                    'class': 'form-control',
                }
            )
        }


class UserProfileForm(ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture']
        widgets = {
            'address_line_1': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'address_line_2': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'city': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'state': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'country': TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }