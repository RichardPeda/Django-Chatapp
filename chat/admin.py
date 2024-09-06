from django.contrib import admin
from chat.models import Message
from chat.models import Chat, Contact

# Register your models here.
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(Contact)