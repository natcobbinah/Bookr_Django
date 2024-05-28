from django.contrib import admin
# from django.contrib.admin import AdminSite

from .models import Publisher, Contributor, Book, \
    BookContributor, Review


class BookAdmin(admin.ModelAdmin):

    search_fields = ('title', 'isbn', 'publisher__name')
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')

    def isbn13(self, obj):
        """
        '9780316769174' => '978-0-31-676917-4'
        """
        return "{}-{}-{}-{}-{}".format(obj.isbn[0:3], obj.isbn[3:4],
                                       obj.isbn[4:6], obj.isbn[6:12],
                                       obj.isbn[12:13])

    list_filter = ('publisher', 'publication_date')


class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',)


class ContributorAdmin(admin.ModelAdmin):
    search_fields = ('last_names__startswith', 'first_names')
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
