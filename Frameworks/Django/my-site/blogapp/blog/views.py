from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def blogs(request):
    return HttpResponse("blogs")

def blog_details(request, id):
    return HttpResponse("blog details: " + str(id))