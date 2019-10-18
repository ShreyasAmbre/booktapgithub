from django.contrib import admin
from book.models import *

admin.site.register(BookType)
admin.site.register(Book)
admin.site.register(EBook)
admin.site.register(BookReviewRecord)