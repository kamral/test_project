from django import forms
from .models import Post,Animation,product

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

