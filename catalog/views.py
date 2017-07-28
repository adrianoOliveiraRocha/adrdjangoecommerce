# coding=utf-8
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import generic


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 3
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list' # optional
    
    
class CategoryListView(generic.ListView):
#    self.kwargs heve the parans nemmed
    template_name = 'catalog/category.html'
    context_object_name = 'product_list' # optional
    paginate_by = 3
    
    def get_catgory(self):
        return get_object_or_404(Category, slug=self.kwargs['slug'])
    
    def get_queryset(self):
        return Product.objects.filter(category=self.get_catgory())

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = self.get_catgory()
        return context
        

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
            'product': product,
            }
    return render(request, 'catalog/product.html', context)
