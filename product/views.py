from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
# Create your views here.
from .forms import PostForm



def index(request):
    posts=Post.objects.all()
    title=Post.objects.get(pk=1)


    return render(request,'index.html',{'posts':posts,'title':title})



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_title_edit(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save()
            post.published_date=timezone.now()
            post.save()
            return redirect('/')

    else:
        form=PostForm(instance=post)
    return render(request,'post_edit.html',{'form':form})
