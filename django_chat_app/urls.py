
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

from chat.views import chat, login_view, register, home, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', lambda req: redirect('/home/')),
    path('chat/', chat, name='chat'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
