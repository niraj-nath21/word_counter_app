from django.shortcuts import render
from django.http import HttpResponse
from .models import features

# Create your views here.

def index(request):
    feature_DB = features.objects.first() # So the models is connected to database and we imported the models here so we are able to access the database.
# So here we are getting the first object from the features table in the DB. Now if we get all() then we'll have to loop through the objects to be able to use the .name and other stuffs.
# But rn there is only one object in the DB so no need to loop through the objects. And if we are using the loop for the frontend then better to loop in the HTML file.
    return render(request, 'index.html', {'feature': feature_DB}) 



def counter(request):
    texts = request.POST['text'] # Here the text is the name of the input field in the HTML form. So renaming the words variable to texts so there is differecnce between the two.
    amount_of_words = len(texts.split())
    return render(request, 'counter.html', {'amount': amount_of_words}) # This 'amount' is the name of the variable that will be used in the HTML file to displat the amount of words.

