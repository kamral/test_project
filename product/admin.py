from django.contrib import admin
from .models import Post, \
    spisok,\
    product, Animation
# Register your models here.

admin.site.register(spisok)
admin.site.register(product)
admin.site.register(Post)
admin.site.register(Animation)



