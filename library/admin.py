from django.contrib import admin
from library.models import *
from django.utils import timezone


class BookInline(admin.StackedInline):
    model = Book
    extra = 1


class CollectionInline(admin.TabularInline):
    model = Collection
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ['pk', 'firstname', 'lastname', 'birth_date', 'is_deleted']
    list_display_links = ['firstname', 'lastname']
    @admin.action(description="Мягкое удаление")
    def update_publish_date(self, request, queryset):
        queryset.update(is_deleted=True)

    # def delete_queryset(self, request, queryset):
    #     # Вместо удаления объектов, изменяем is_deleted
    #     queryset.update(is_deleted=True)

    actions = ['update_publish_date']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [CollectionInline]
    list_display = [
        'pk',
        "title",
        'author_id',
        'category_id',
        'publish_date',
    ]

    list_display_links = ['title']

    @admin.action(description="Опубликовано сегодня")
    def update_publish_date(self, request, queryset):
        queryset.update(publish_date=timezone.now())

    actions = [update_publish_date]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    inlines = [CollectionInline]
    list_display = ['pk', 'name']
    list_display_links = ['name']
    pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    inlines = [BookInline]
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
