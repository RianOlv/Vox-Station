from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import login as auth_login
from django.contrib import messages


def NewContaView(request):
    newconta = RegistrationForm(request.POST or None)

    if newconta.is_valid():
        user = newconta.save(commit=False)
        password = newconta.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        auth_login(request, new_user)
        return render(request, './inicio/index.html', {'user': user})

    return render(request, './login/create_conta.html', {'newconta': newconta})


def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request, './inicio/index.html', {'user': user})
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    else:
        form = AuthenticationForm()
    return render(request, './login/logar_conta.html', {'form': form})

