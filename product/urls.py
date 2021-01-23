from django.urls import path

from .views import product_name_edit
from .views import Index, \
    PostDetail,\
    PostTitleEdit,\
    AnimationAdd,\
    AnimationDelete, ProductDetail,ProductAdd,ProductDelete,ProductNameEdit

urlpatterns = [
    path('',Index.as_view(), name='home'),
    # path('',index),
    # path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_edit'),
    # path('post/<int:pk>/edit/', post_title_edit, name='post_edit'),
    path('post/<int:pk>/edit/', PostTitleEdit.as_view(), name='post_edit'),
    # path('post/add_photo/', add_photo, name='add_photo'),
    path('post/add_photo/', AnimationAdd.as_view(), name='add_photo'),
    # path('post/<int:pk>/delete/', delete_photo, name='animation_delete')
    path('animation_delete/<int:pk>/delete/', AnimationDelete.as_view(),
         name='animation_delete'),
    # path('product/<int:pk>/', produtc_detail, name='product_detail')
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    # path('product/product_add/', product_add, name='product_add')
    path('product/product_add/', ProductAdd.as_view(), name='product_add'),
    # path('product/<int:pk>/delete/', product_delete, name='product_delete')
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    # path('product/<int:pk>/edit/', product_name_edit, name='product_name_edit'),
    path('product/<int:pk>/edit/', ProductNameEdit.as_view(), name='product_name_edit'),

]