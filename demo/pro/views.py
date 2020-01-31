from django.shortcuts import render
from pro.models import Register


def register(request):

    if request.method == 'POST':
        # username = request.POST.get('username', False)
        customer = request.POST.get('customer', False)
        print(type(customer))
        supplier = request.POST.get('supplier', False)

        user = Register.objects.create(cutomer=customer, supplier=supplier)
        user.save()
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')