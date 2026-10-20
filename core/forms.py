from django import forms
from django.contrib.auth.models import User
import re

class RegistroForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")
    username = forms.CharField(max_length=150, required=True, label="Nombre de usuario")
    email = forms.EmailField(required=True, label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'[a-zA-Z]', password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra.")
        if not re.search(r'\d', password):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        if not re.search(r'[^a-zA-Z0-9]', password):
            raise forms.ValidationError("La contraseña debe contener al menos un símbolo o signo (ej. @, #, $, etc.).")
            
        return password
    