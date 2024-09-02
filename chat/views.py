from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from chat.models import Message,Chat
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    contacts = User.objects.exclude(username = request.user)        
        
    return render(request, 'chat/home.html', {'contacts': contacts})



@login_required(login_url='/login/')
def index(request):
    if(request.method == 'POST'):
        mychat = Chat.objects.get(id=1)
        print(request.user)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=mychat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [new_message])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    if(request.method == 'GET'):

        myuser = request.GET.get('user')
        print(myuser)

        chatmessages = Message.objects.filter(chat__id=1)
        return render(request, 'chat/index.html', {'messages': chatmessages})
    

def login_view(request):
    if(request.method == 'POST'):
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])

        if user:
            login(request, user)
            return HttpResponseRedirect('/home/')   
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True})
    return render(request, 'auth/login.html')

def register(request):
    if(request.method == 'POST'):
        name = request.POST['username']
        passwort_1 = request.POST['password']
        passwort_2 = request.POST['passwordConfirm']
        if passwort_1 == passwort_2:
            user = User.objects.create_user(username=name, password=passwort_1)

        if user:
            return HttpResponseRedirect('/login/')   
        else:
            return render(request, 'auth/register.html', {'wrongPassword': True})
    return render(request, 'auth/register.html')
