from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth # Importing the User model from django.contrib.auth.models to create a new user.
from django.contrib import messages  # Importing messages to display success or error messages to the user.
from .models import features

# Create your views here.

def index(request):
    feature_DB = features.objects.first() # So the models is connected to database and we imported the models here so we are able to access the database.
# So here we are getting the first object from the features table in the DB. Now if we get all() then we'll have to loop through the objects to be able to use the .name and other stuffs.
# But rn there is only one object in the DB so no need to loop through the objects. And if we are using the loop for the frontend then better to loop in the HTML file.
    return render(request, 'index.html', {'feature': feature_DB}) 


def register(request):
    if request.method == "POST":
        # This is the register page. So when the user submits the form, the data will be sent to the server and we can access it using request.POST.
        username = request.POST.get('username') # Here we are getting the username from the POST request. So when the user submits the form, the data will be sent to the server and we can access it using request.POST.
        password = request.POST.get('password') # Same for the password. So we are getting the username and password from the POST request.
        email = request.POST.get('email') 
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register') # If the username already exists, we are redirecting the user to the register page again.
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists') # If the email already exists, we are redirecting the user to the register page again.
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                # Now in the above line the 'user' is the variable that will hold the user object that we created. 
                # create_user is creating a new user with the given username, password and email.
                # And the value of username will be stored in the username field of the User model, same for password and email.
                user.save() # Saving the user to the database.
                return redirect('login') # After the user is created, we are redirecting the user to the login page.
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register') # If the passwords do not match, we are redirecting the user to the register page again.
    else:
        return render(request, 'register.html') # This is the register page. So we are rendering the register.html file here. And this will be used to register the user in the future.


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password) # This is used to authenticate the user. So we are checking if the username and password match with the user in the database.
    
        if user is not None:
            auth.login(request, user) # If the user is authenticated, we are logging the user in.
            return redirect('/') 
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def counter(request):
    texts = request.POST['text'] # Here the text is the name of the input field in the HTML form. So renaming the words variable to texts so there is differecnce between the two.
    amount_of_words = len(texts.split())
    return render(request, 'counter.html', {'amount': amount_of_words}) # This 'amount' is the name of the variable that will be used in the HTML file to displat the amount of words.

def post(request, pk):
    return render(request, 'post.html', {'pk': pk}) 

