from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Product, Category

# def create_product(request):
#     Product.objects.bulk_create([
#     Product(name="Tablet", price=400),
#     Product(name="Monitor", price=300),
# ])
#     return HttpResponse(f"Created")


# def active_products_view(request):
#     active_products = Product.objects.filter(is_active=True)

#     result = ""
#     for p in active_products:
#         result += f"{p.name} - {p.price}<br>"

#     return HttpResponse(result)


def test_run(request):
    # text=''
    # results = Product.objects.values('name', 'price')
    # for p in results:
    #     text += f"{p['name']} - {p['price']}<br>"
    # return HttpResponse(text)


    # text=''
    # results = Product.objects.values_list('name')
    # print(results)
    # return HttpResponse(results) # as tuples

    # result = Product.objects.filter(price__gt=100)
    # print(result[1].id)
    # return HttpResponse(result)


    # product, created = Product.objects.get_or_create(
    #     name="Mouse",
    #     defaults={"price": 50})
    # print(product)
    # return HttpResponse(created)

#     Product.objects.create(
#     name="Calculator",
#     price=100,
#     is_active=True
# )
#     return HttpResponse('created')







#     Category.objects.create(name="Electronics")
#     cat = Category.objects.filter(name="Electronics").first()
#     Product.objects.create(
#     name="Laptop",
#     price=1200,
#     category=cat
# )
#     result = Product.objects.filter(price__gt = 1000)
#     print(result)
#     return HttpResponse('created')

    # product = Product.objects.get(id=1)
    # print(product.category.name)
    # return HttpResponse('created')

    # category = Category.objects.get(id=1)
    # results = category.products.all()
    # print(results)
    # return HttpResponse('created')

    # results = Product.objects.filter(category__name="Electronics")
    # print(results)
    # return HttpResponse('created')

    # results = Category.objects.filter(products__price__gt=1000)
    # print(results)
    # return HttpResponse('created')

    results = Product.objects.select_related('category')
    print(results)
    return HttpResponse('created')









