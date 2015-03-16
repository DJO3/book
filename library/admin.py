from django.contrib import admin
from library.models import Author, Book


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth', 'wiki')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)