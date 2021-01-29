from django import forms
from .models import Post,Animation,product,spisok,Email

class PostForm(forms.ModelForm):


    class Meta:
        model=Post
        fields=['title']


class AnimationForm(forms.ModelForm):

    class Meta:
        model=Animation
        fields=['photo']



class ProductForm(forms.ModelForm):

    class Meta:
        model=product
        fields='__all__'


class ProductProductNameEditForm(forms.ModelForm):

    class Meta:
        model=product
        fields=('product_name',)



class ProductAddPhoto(forms.ModelForm):

    class Meta:
        model=product
        fields=('product_photo',)


class ProductEditSpisok(forms.ModelForm):

    class Meta:
        model=spisok
        fields=('title',)



class EmailForm(forms.ModelForm):

    class Meta:
        model=Email
        fields='__all__'