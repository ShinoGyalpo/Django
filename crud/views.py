from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog #object

# Create your views here.
def index(request):
    blog = Blog.objects.all()
    
    return render(request, "crud/index.html", {"blogs":blog})

def about(request):
    return render(request,"crud/about.html")