from django.contrib import admin
from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publish", "status"]
    list_filter = ["status", "created", "publish", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "post", "created", "active"]
    list_filter = ["active", "created"]
    search_fields = ["name", "email", "body"]


# Shell commands for navigating through the database.
# Leveraging on filter commands.
# Filtering the exact match
# Post.objects.filter(title__contains='Django') returns titles with the word Django and is not case sensitive.
# Post.objects.filter(title__icontains='Django') is case sensitive.
