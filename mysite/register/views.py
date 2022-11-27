from .forms import UserForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import auth


class LoginView(View):

    def get(request):
        form = UserForm()
        if "sign-in" in request.GET:
            username = request.GET.get("username")
            password = request.GET.get("pswd")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Login attemp failed.')
                return redirect('registration/login.html')
        return render(request, 'registration/login.html', {'form': form})

    def register(response,):
        if response.method == "POST":
            form = RegisterForm(response.POST)
            if form.is_valid():
                form.save()
                messages.success(response, "account created succefuly")
                return redirect("/")
            messages.error(response, "error")
            return render(response, "register/register.html", {"form": form})
        else:
            form = RegisterForm()
            messages.warning(response, "error")
        return render(response, "register/register.html", {"form": form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out succesfully.')
        return redirect('account_login')
