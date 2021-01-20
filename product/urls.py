from django.urls import path
from .views import index,posts_edit

urlpatterns = [
    path('',index),
    path('post/<int:pk>/',posts_edit,name='post_edit')
]