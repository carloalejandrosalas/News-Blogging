from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'subtitle', 'registered_at')
    # list_filter = ('choice_text',)


admin.site.register(Post, PostAdmin)