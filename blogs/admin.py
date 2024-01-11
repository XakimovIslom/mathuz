from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    list_display = ('id', 'title', 'category', 'created_at',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'tag')
    readonly_fields = ('created_at',)
    fields = ('title', 'category', 'tag', 'content', 'created_at',)



admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(About)
