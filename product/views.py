from django.shortcuts import render
from .models import post
# Create your views here.

def index(request):
    posts=post.objects.all()
    title=post.objects.get(pk=1)

    return render(request,'index.html', {
        'posts':posts,'title':title})