from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  

@admin.action(description='Mark selected posts as featured')
def make_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_featured')
    
    list_filter = ('author', 'created_at', 'is_featured')
    
    search_fields = ('title', 'content')
    
    ordering = ('-created_at',)
    
    date_hierarchy = 'created_at'
    
    inlines = [CommentInline]
    
    actions = [make_featured]
    
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'author')
        }),
        ('Content', {
            'fields': ('content', 'is_featured'),
            'classes': ('collapse',), 
        }),
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)