from django.shortcuts import render
from rest_framework.decorators import api_view
from ElectronicBook.models import Book
from customer.models import CustomerOrders
from pro.models import Signin


# Below code is fro Number of Entries in Book Table Useful for Analysis
@api_view(['GET'])
def count(request):
    if request.method == 'GET':
        book_count = Book.objects.count()
        customer_count = Signin.objects.filter(is_customer=True).count()
        supplier_count = Signin.objects.filter(is_suppliers=True).count()
        order_success_count = CustomerOrders.objects.filter(paid=True ).count()
        # count_insert = NoOfBooks.objects.create(total_books=count)
        # count_insert.save()
        return render(request, 'dashboard.html', {'Count': book_count, 'Customer_Count': customer_count,
                                                  'Supplier_Count': supplier_count,
                                                  'Order_Success_Count': order_success_count})
