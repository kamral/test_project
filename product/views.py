from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post,Animation,product
# Create your views here.
from .forms import PostForm,PostPhotoForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView,DetailView,UpdateView,DeleteView, CreateView
from django.urls import reverse_lazy

class Index(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.get(pk=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        contex=super().get_context_data(**kwargs)
        contex['title']=Post.objects.get(pk=1)
        contex['animation']=Animation.objects.all()
        contex['product']=product.objects.all()
        return contex

# def index(request):
#     posts=Post.objects.all()
#     title=Post.objects.get(pk=1)
#     animation=Animation.objects.all()
#
#
#     return render(request,'index.html',
#                   {'posts':posts,
#                    'title':title,
#                    'animation':animation})



class PostDetail(DetailView):
    template_name = 'post_detail.html'
    model = Post



    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['post']=Post.objects.get(pk=1)
        return context


#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'post_detail.html', {'post': post})




class PostTitleEdit(UpdateView):
    model = Post
    fields = ['title']
    success_url = '/'
    template_name = 'post_edit.html'
    context_object_name = 'photo'

# def post_title_edit(request,pk):
#     post=get_object_or_404(Post,pk=pk)
#     if request.method == 'POST':
#         form=PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post=form.save()
#             post.published_date=timezone.now()
#             post.save()
#             return redirect('/')
#
#     else:
#         form=PostForm(instance=post)
#     return render(request,'post_edit.html',{'form':form})



class PhotoAdd(CreateView):
    model=Animation
    template_name = 'add_photo.html'
    fields = ['photo']
    success_url = '/'

# def add_photo(request):
#     if request.method == 'POST':
#         photo=PostPhotoForm(request.POST,request.FILES)
#         if photo.is_valid():
#             photo.save()
#             return redirect('/')
#     else:
#         photo=PostPhotoForm()
#     return render(request,'add_photo.html', {'form':photo})


class PhotoDelete(DeleteView):
    model = Animation
    template_name = 'delete_photo.html'
    success_url = reverse_lazy('home')





#
# def delete_photo(request,pk):
#     photo=Animation.objects.get(pk=pk)
#     photo.delete()
#     context={'delete_photo':photo}
#     return render(request, 'delete_photo.html', context)
#




class ProductDetail(DetailView):
    model = product
    template_name = 'product_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['products'] = product.objects.all()

        return contex

def product_detail(request,pk):
    products=get_object_or_404(product,pk=pk)
    return render(request,'product_detail.html', {'products':products})
