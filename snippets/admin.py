from django.contrib import admin
from snippets.models import Snippet
# Register your models here.

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'language', 'style', 'owner')


admin.site.register(Snippet, SnippetAdmin)