from django.contrib import admin
from library.models.authors import Author



# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
