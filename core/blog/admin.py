from django.contrib import admin

from blog.models import Post,Category

class PostAdmin(admin.ModelAdmin):
    list_display=['author','title','status','category','created_date','published_date']

admin.site.register(Post)
admin.site.register(Category)