from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post,Animation,product,MapCoordinates,spisok,punkt_of_spisok
# Create your views here.
from .forms import \
    PostForm,\
    AnimationForm,\
    ProductForm,\
    ProductProductNameEditForm,ProductAddPhoto
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView,\
    DetailView,\
    UpdateView,\
    DeleteView,\
    CreateView
from django.urls import reverse_lazy

class Index(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.get(pk=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        contex=super().get_context_data(**kwargs)
        contex['title']=Post.objects.get(pk=1)
        contex['animation']=Animation.objects.all()
        contex['product']=product.objects.all().order_by('created_date')
        contex['map']=MapCoordinates.objects.all()
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



class AnimationAdd(CreateView):
    model=Animation
    template_name = 'add_photo.html'
    fields = ['photo']
    success_url = '/'

# def add_photo(request):
#     if request.method == 'POST':
#         photo=AnimationForm(request.POST,request.FILES)
#         if photo.is_valid():
#             photo.save()
#             return redirect('/')
#     else:
#         photo=PostPhotoForm()
#     return render(request,'add_photo.html', {'form':photo})


class AnimationDelete(DeleteView):
    model = Animation
    template_name = 'delete_photo.html'
    success_url = reverse_lazy('home')
    context_object_name = 'product_delete'





#
# def delete_photo(request,pk):
#     photo=Animation.objects.get(pk=pk)
#     photo.delete()
#     context={'delete_photo':photo}
#     return render(request, 'delete_photo.html', context)
#




# class ProductDetail(ListView):
#     model = product
#     template_name = 'product_detail.html'
#
#
#     def get_queryset(self):
#         return product.objects.filter(pk=self.kwargs['pk'])
#
#     def title_spisok(self):
#         return spisok.objects.filter(product=self.kwargs['pk'])
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['products']=product.objects.filter(pk=self.kwargs['pk'])
#         context['title_product']=spisok.objects.filter(product=self.kwargs['pk'])
#         spisoks = spisok.objects.filter(pk=self.kwargs['pk'])
#         context['punkt_of_spisoks1'] = punkt_of_spisok.objects.filter(spisok=spisoks)
#
#
#         return context




def product_detail(request,pk):
    products=product.objects.filter(pk=pk)
    title_spisok=spisok.objects.filter(product=pk)
    # spisok1=title_spisok.filter(spisok=pk)


    punkt=punkt_of_spisok.objects.filter(spisok__product=pk)


    return render(request,'product_detail.html', {'products':products,
                                                  'title_product':title_spisok,
                                                  'punkts1':punkt,
                                                  # 'spisok1':spisok1
                                                  })



class ProductAdd(CreateView):
    model =product
    fields = '__all__'
    template_name = 'product_add.html'
    success_url = '/'



# def product_add(request):
#     if request.method=='POST':
#         form=ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product=form.save()
#             return redirect('/')
#
#     else:
#         form=ProductForm()
#
#     return render(request, 'product_add.html', {'form':form})


class ProductDelete(DeleteView):
    model = product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('home')


#
# def product_delete(request,pk):
#     products=get_object_or_404(product,pk=pk)
#     products.delete()
#     context={'product_delete':products}
#     return  render(request,'product_delete.html', context)



class ProductNameEdit(UpdateView):
    model=product
    template_name = 'product_detail_product_name_edit.html'
    success_url = '/'
    fields = ['product_name',]




# def product_name_edit(request,pk):
#     product_name_edit=get_object_or_404(product, pk=pk)
#     if request.method == 'POST':
#         form=ProductProductNameEditForm(request.POST,instance=product_name_edit)
#         if form.is_valid():
#             product_name_edit=form.save()
#             product_name_edit.save()
#             return redirect('home')
#     else:
#         form=ProductProductNameEditForm()
#
#     return render(request, 'product_detail_product_name_edit.html',{'form':form})




def product_detail_add_photo(request):
    if request.method == 'POST':
        form=ProductAddPhoto(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ProductAddPhoto()
    return render(request, 'product_detail_add_photo.html',{'form':form})


def product_detail_photo_delete(request,pk):
    try:
        person = product.objects.get(pk=pk)
        person.delete()
        return HttpResponseRedirect("/")
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


