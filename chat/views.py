from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from chat.models import Message, Chat, Contact
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/login/')
def home(request):

    if (request.method == 'POST'):
        contact = request.POST['contact']
        obj_contact = Contact.objects.get(contact = contact)
       
        this_chat, created = Chat.objects.get_or_create(author = request.user, receiver = obj_contact)
        chat_id = this_chat.id
        # print('dieser chat', this_chat.id)

        # chat_id = this_chat.values_list('id', flat=True).first()
        
        # this_chat = Chat.objects.filter(author = request.user, receiver = obj_contact.id)
        # chat_id = this_chat.values_list('id', flat=True).first()
        # print(chat_id)
        # if not this_chat:
        #     print('empty_chat1')
            
        #     this_chat = Chat.objects.filter(receiver = request.user, author = obj_contact.id)
        #     chat_id = this_chat.values_list('id', flat=True).first()
            
        #     if not this_chat:  
        #         print('empty_chat2')
        #         this_chat = Chat.objects.create(author = request.user, receiver = obj_contact)
        #         chat_id = this_chat.id
        #         print('chat erstellt', this_chat.id)
        if this_chat:
            print('chat gefunden')
          
            # print(this_chat.values())
            # chat_id = this_chat.values_list('id', flat=True).first()
           
            return HttpResponse(str(chat_id))

    if(request.method == 'GET'):

        contacts = Contact.objects.all()     
        return render(request, 'chat/home.html', {'contacts': contacts})



@login_required(login_url='/login/')
def create_chat(request):
    pass
    

                

@login_required(login_url='/login/')
def chat(request):
    chat_id = request.GET.get('id')
    mychat = Chat.objects.get(id=chat_id)
   
    if (request.method == 'POST'):
        

        print(mychat.receiver)
        
        
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=mychat, author=request.user, receiver=mychat.receiver)
        serialized_obj = serializers.serialize('json', [new_message])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    if (request.method == 'GET'):
        contacts = Contact.objects.all()     
        receiver = mychat.receiver.contact
        chatmessages = Message.objects.filter(chat__id=chat_id)
     
        return render(request, 'chat/chatroom.html',  {'messages' : chatmessages, 'id' : chat_id, 'receiver' : receiver, 'contacts':contacts})



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
            Contact.objects.get_or_create(contact = 'Mario', male = True)
            Contact.objects.get_or_create(contact = 'Helena', male = False)
            Contact.objects.get_or_create(contact = 'Florian', male = True)
            Contact.objects.get_or_create(contact = 'Anna', male = False)

        if user:
            return HttpResponseRedirect('/login/')   
        else:
            return render(request, 'auth/register.html', {'wrongPassword': True})
    return render(request, 'auth/register.html')
