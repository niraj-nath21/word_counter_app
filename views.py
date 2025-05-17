from django.shortcuts import render
from django.http import HttpResponse
from .models import features

# Create your views here.

def index(request):
    feature1 = features()
    feature1.id = 1
    feature1.name = "Word Counter App"
    feature1.details = "This is a word counter app that counts the number of word in a given text."
    feature1.text_area = "Enter your text here...."
    return render(request, 'index.html', {'feature': feature1}) 

def counter(request):
    texts = request.POST['text'] # Here the text is the name of the input field in the HTML form. So renaming the words variable to texts so there is differecnce between the two.
    amount_of_words = len(texts.split())
    return render(request, 'counter.html', {'amount': amount_of_words}) # This 'amount' is the name of the variable that will be used in the HTML file to displat the amount of words.

