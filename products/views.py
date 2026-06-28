from django.shortcuts import render

from .models import Product, Category, Tag


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    query = request.GET.get("q", "")
    category_id = request.GET.get("category", "")
    tag_ids = request.GET.getlist("tags")  # getlist handles multiple tag selections

    if query:
        products = products.filter(description__icontains=query)
    if category_id:
        products = products.filter(category__id=category_id)
    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()

    context = {
        "products": products,
        "categories": categories,
        "tags": tags,
        "query": query,
        "selected_category": category_id,
        "selected_tags": tag_ids,
    }
    return render(request, "products/product_list.html", context)
