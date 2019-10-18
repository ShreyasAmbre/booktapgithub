from django.contrib import admin

# Register your models here.
from customer.models import *


admin.site.register(CustomerOrders)
admin.site.register(CustomerSearch)
admin.site.register(CustomerReview)

