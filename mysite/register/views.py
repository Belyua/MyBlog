from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views import View
from .forms import RegisterForm
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
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        if "sign-up" in request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                selected_group = request.POST.get("groups")
                group = Group.objects.get(name=selected_group)
                user.groups.add(group)
                messages.success(request, 'Account has been created succesfully')
                return redirect('account_login')
            else:
                messages.error(request, form.errors)
                return redirect('account_login')
        return render(request, '/')


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out succesfully.')
        return redirect('account_login')


def register(response,):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'Account has been created succesfully')
        else:
            messages.error(response, "not valid form, try again")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
#
#
# def login(response):
#     if response.method == 'POST':
#         user = auth.authenticate(username=response.POST['username'],
#                                  password=response.POST['password'])
#         if user is not None:
#             auth.login(response, user)
#             return render(response, '/')
#         else:
#             return render(response, '/', {"error": "invalid login credentials"})
#     return render(response, 'registration/login.html')