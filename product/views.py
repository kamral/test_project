from django.shortcuts import render
from .models import post
# Create your views here.
from .forms import PostForm



def index(request):
    posts=post.objects.all()
    title=post.objects.get(pk=1)


    return render(request,'index.html', {
        'posts':posts,'title':title})



def posts_edit(request):
    if request.method == 'POST':
        post_edit = PostForm(request.POST)
        if post_edit.is_valid():
            post_edit.save()

    else:
        post_edit = PostForm()

    return render(request,'post_edit.html',{'form':post_edit})
