from django.contrib import admin
from ElectronicBook.models import *

admin.site.register(BookType)
admin.site.register(Book)
admin.site.register(ElectronicBook)
admin.site.register(BookReviewRecord)