from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def counter(request):
    texts = request.POST['text'] # Here the text is the name of the input field in the HTML form. So renaming the words variable to texts so there is differecnce between the two.
    amount_of_words = len(texts.split())
    return render(request, 'counter.html', {'amount': amount_of_words}) # This 'amount' is the name of the variable that will be used in the HTML file to displat the amount of words.

