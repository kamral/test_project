from django.shortcuts import render
from .models import post
# Create your views here.

def index(request):
    news=post.objects.all()
    title=post.objects.get(title__contains='Название поста')
    return render(request,'index.html', {'news':news,'title':title})