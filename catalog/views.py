# coding=utf-8
#nao esquecer de colocar get_object_or_404
from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import Product, Category


# def product_list(request):
#     context = {
#        'product_list': Product.objects.all()
#     }
#     return render(request, 'catalog/product_list.html', context)

class ProductListView(generic.ListView):

    queryset = Product.objects.all()
    #model = Product
    template_name = 'catalog/product_list.html'
    #aqui posso cosmotizar as views como nome que eu quero chamar no template dentro da pagina produtc_list.html
    context_object_name = 'produtos'
    paginate_by = 3

product_list = ProductListView.as_view()

class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'produtos'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()

# def category(request, slug):
#     category = Category.objects.get(slug=slug)
#     context = {
#         'current_category': category,
#         'product_list': Product.objects.filter(category=category),
#     }
#     return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
