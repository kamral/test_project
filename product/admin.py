from django.contrib import admin
from .models import post, spisok, product
# Register your models here.

admin.site.register(spisok)
admin.site.register(product)
admin.site.register(post)


