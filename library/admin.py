from django.contrib import admin
from library.models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass