from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.views import View
from .forms import UserForm


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
