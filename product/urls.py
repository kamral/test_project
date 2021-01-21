from django.urls import path
from .views import index, post_detail,post_title_edit

urlpatterns = [
    path('',index),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', post_title_edit, name='post_edit'),

]