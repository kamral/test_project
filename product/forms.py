from django import forms
from .models import Post,Animation

class PostForm(forms.ModelForm):


    class Meta:
        model=Post
        fields=['title']


class PostPhotoForm(forms.ModelForm):

    class Meta:
        model=Animation
        fields=['photo']