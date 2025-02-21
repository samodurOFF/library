from django.contrib import admin
from library.models import *


class BookInline(admin.StackedInline):
    model = Book
    extra = 1
    classes = ['collapse']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ('pk', 'firstname', 'lastname', 'birth_date', 'is_deleted')
    list_display_links = ('firstname', 'lastname')


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
