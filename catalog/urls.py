from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/category-distribution/', views.category_distribution, name='category_distribution'),
    path('', RedirectView.as_view(url='products/')),
    path('products/table-template/', views.product_table_template, name='product_table_template'),
]


