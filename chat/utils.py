from chat.models import Message, Chat, Contact

def create_Contacts():
    """
    This function creates four contacts for testing the app
    """
    Contact.objects.get_or_create(contact = 'Mario', male = True)
    Contact.objects.get_or_create(contact = 'Helena', male = False)
    Contact.objects.get_or_create(contact = 'Florian', male = True)
    Contact.objects.get_or_create(contact = 'Anna', male = False)