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

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fields = [
        "name",
        'surname',
        'email',
        'gender',
        'birth_date',
        'role',
        'is_active',
        'libraries',
    ]

    list_display = (
        "name",
        'surname',
        'age',
    )

    class Meta:
        model = Category
        fields = "__all__"
