from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'),
    path('catalog/', views.CatalogViews.as_view(), name='catalog_all'),
    path('catalog/<slug:category_slug>/', views.CatalogViews.as_view(), name='catalog'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]