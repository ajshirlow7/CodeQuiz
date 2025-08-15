from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    """
    Render the home page of the CodeQuiz application.
    """
    return render(request, 'home.html')