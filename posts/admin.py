from django.contrib import admin
from posts.models import Post

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(Post)
