from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Tag, Post, User

# Register your models here.
admin.site.register(User)
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Tag)
