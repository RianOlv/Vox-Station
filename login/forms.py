from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, label='Nome de usuário', max_length=20, required=True)
    email = forms.EmailField(widget=forms.EmailInput, label='Endereço de email', required=True)
    email2 = forms.EmailField(widget=forms.EmailInput, label='Confirmação de email', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Senha', required=True, max_length=32)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmação de senha', required=True, max_length=32)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]
        # Colocar novos campos e suas respectivas validações depois!!

    password_aux = ''

    def clean_password(self):
        global password_aux

        password = self.cleaned_data.get('password')
        password_aux = password
        msg = ''

        # --> Verifica o tamanho da senha
        min_length = 8
        if len(password) < min_length:
            msg = 'A senha deve conter no mínimo %s caracteres.' % (str(min_length))
            raise forms.ValidationError(msg)

        if msg == '':
            # --> Verifica se há números na senha
            if sum(c.isdigit() for c in password) < 1:
                msg = 'A senha deve conter no mínimo 1 número.'
                raise forms.ValidationError(msg)

        if msg == '':
            # --> Verifica se há letras maiúsculas na senha
            if not any(c.isupper() for c in password):
                msg = 'A senha deve conter letras maiúsculas e minúsculas.'
                raise forms.ValidationError(msg)

        if msg == '':
            # --> Verifica se há letras minúsculas na senha
            if not any(c.islower() for c in password):
                msg = 'A senha deve conter letras maiúsculas e minúsculas.'
                raise forms.ValidationError(msg)

        return password_aux

    def clean_password2(self):
        global password_aux

        password2 = self.cleaned_data.get('password2')

        if password_aux != password2:
            raise forms.ValidationError('As senhas devem ser iguais.')
        return password_aux

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        email_qs = User.objects.filter(email=email)

        if email != email2:
            raise forms.ValidationError('Os emails devem ser iguais.')

        if email_qs.exists():
            raise forms.ValidationError('Esse email já está cadastrado.')
        return email

