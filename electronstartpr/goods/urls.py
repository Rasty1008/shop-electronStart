from django.urls import path
from django.views.decorators.cache import cache_page
from goods import views

app_name = 'catalog'

urlpatterns = [
    path('', views.CatalogListView.as_view(), name='index'),
    path('search/', views.CatalogListView.as_view(), name='search'),
    path('product/<slug:product_slug>/', cache_page(60 * 10) (views.ProductDetailView.as_view()), name='product'),
    path('<slug:category_slug>/', views.CatalogListView.as_view(), name='category'),
    

]