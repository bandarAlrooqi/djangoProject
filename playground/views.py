from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, OrderItem
from django.db.models import Q, F  # Q for queries, F for fields


def say_hello(request):
    query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id')).order_by('title')
    # for more info about the query set, see:
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/
    return render(request, 'hello.html', {'name': 'Bandar', 'products': list(query_set)})
