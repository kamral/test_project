from django.shortcuts import render
from .models import post
# Create your views here.

def index(request):
    news=post.objects.all()
    return render(request,'index.html', {'news':news})