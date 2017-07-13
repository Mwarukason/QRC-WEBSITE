from django.contrib import admin

# Register your models here.
from .models import Post

#Customizing the admin.
class PostModelAdmin(admin.ModelAdmin):
    #adding customised admin field
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "body"]

    class Meta:
        model = Post
        
#Connect admin and class PostModelAdmin
admin.site.register(Post, PostModelAdmin)
