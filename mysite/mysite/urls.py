from django.contrib import admin
from django.urls import path, include
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.LoginView.register, name="register"),
    path("login/", views.LoginView.get, name="login"),
    path('', include('blog.urls')),
    path('', include("django.contrib.auth.urls")),

]
