from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Edición").exists():
            return ('published', 'author', 'categories')
        else:
            return ('created', 'updated')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"  