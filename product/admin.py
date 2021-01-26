from django.contrib import admin
from .models import Post, \
    spisok,\
    product, Animation,MapCoordinates,punkt_of_spisok
# Register your models here.





class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'name_productions','created_date',
                    'published_date',)
    list_filter = ('created_date','title','name_productions')
    search_fields = ('title',)

class SpisokAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title_number','product_name','product_photo')
    search_fields = ('title_number',)
    list_filter = ('title_number',)



class AnimationAdmin(admin.ModelAdmin):
    list_display = ('photo',)
    list_filter = ('photo',)




admin.site.register(punkt_of_spisok)
admin.site.register(spisok,SpisokAdmin)
admin.site.register(product,ProductAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Animation,AnimationAdmin)
admin.site.register(MapCoordinates)



