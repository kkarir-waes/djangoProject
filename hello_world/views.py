from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):

    if requests == "POST":
        return HttpResponse("You POSTED something")
    else:
        return HttpResponse(requests.method)



