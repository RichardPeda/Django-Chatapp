# Simple Chat App
 A simple chat app written with Django 5.1.
 
 A user can register and login. With the new registration of a user, four imaginary contacts will be created. These contacts are only for testing the app. The user can open a private chat by clicking a contact and write messages. 

### Requirements
You have to install the latest Python version on your computer.
https://www.python.org/downloads/

 ## Installation
 1. Clone this repository
 2. Create a virtual environment `python -m venv env`
 3. Activate the virtual environment `"env/Scripts/activate"`
 4. then you can run
    
 ```
 pip install requirements.txt
```
 3. Go to the folder "django_chat_app"
 4. Generate the database with command `python manage.py migrate`
 5. Run the command `python manage.py createsuperuser` to have access to the admin page
 6. Run the command `python manage.py runserver` to start the app on your machine
