from django.contrib import admin

# Register your models here.
from .models import Book

class AdminBook(admin.ModelAdmin):
    list_display = ["__str__", "author", "release", "timestamp"]
    list_filter =  ["timestamp"]
    list_display_links = ["author"]
    list_editable = ["release"]
    search_fields = ["__str__", "author"]
    class Meta:
        model = Book
        
admin.site.register(Book, AdminBook)