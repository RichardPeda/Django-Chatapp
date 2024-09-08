from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from chat.models import Message, Chat, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from chat.utils import create_Contacts


@login_required(login_url='/login/')
def home(request):
    """
    *This function returns the html start page with all existing contacts.*
    *A post request creates a new chat if not existing and return the chat id.*
    """
    if (request.method == 'POST'):
        contact = request.POST['contact']
        obj_contact = Contact.objects.get(contact = contact)
        this_chat, created = Chat.objects.get_or_create(author = request.user, receiver = obj_contact)
        chat_id = this_chat.id
        if this_chat:
            return HttpResponse(str(chat_id))

    if(request.method == 'GET'):
        contacts = Contact.objects.all()     
        return render(request, 'chat/home.html', {'contacts': contacts})


@login_required(login_url='/login/')
def chat(request):
    """
    This function returns the html chat-page of the active chat based of the given id.
    A post request creates a new chat message and returns it as JSON
    """
    chat_id = request.GET.get('id')
    mychat = Chat.objects.get(id=chat_id)
   
    if (request.method == 'POST'):    
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=mychat, author=request.user, receiver=mychat.receiver)
        serialized_obj = serializers.serialize('json', [new_message])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    if (request.method == 'GET'):
        contacts = Contact.objects.all()     
        receiver = mychat.receiver.contact
        chatmessages = Message.objects.filter(chat__id=chat_id)
        return render(request, 'chat/chatroom.html',  {'messages' : chatmessages, 'id' : chat_id, 'receiver' : receiver, 'contacts':contacts})


def login_view(request):
    """
    A GET-request returns the html of the login page
    A POST-request checks the database if the user exist and response a JSON if this authentification was successfull.
    """
    if(request.method == 'POST'):
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        if user:
            login(request, user)
            return JsonResponse({"success":True})    
        else:
            return JsonResponse({"success":False})    
    if(request.method == 'GET'):
        return render(request, 'auth/login.html')


def register(request):
    """
    A GET-request return the html of the register page.
    A POST-request compares the given passwords and creates a new user and four contacts for testing the app.
    The function returns a JSON when is was successfull.
    """
    if(request.method == 'POST'):
        name = request.POST['username']
        email = request.POST['email']
        passwort_1 = request.POST['password']
        passwort_2 = request.POST['passwordConfirm']
        if passwort_1 == passwort_2:
            user = User.objects.create_user(username=name, password=passwort_1, email=email)
            create_Contacts()
        if user:
            return JsonResponse({"success":True})   
        else:
            return render(request, 'auth/register.html', {'wrongPassword': True})
    return render(request, 'auth/register.html')


def logout_view(request):
    """
    The function logs the current user out and returns a JSON to redirect in the frontend.
    """
    logout(request) 
    return JsonResponse({"redirect": True})
