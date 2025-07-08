from django.urls import path

from goods import views

app_name = 'catalog'

urlpatterns = [
    path('', views.CatalogListView.as_view(), name='index'),
    path('search/', views.CatalogListView.as_view(), name='search'),
    path('product/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product'),
    path('<slug:category_slug>/', views.CatalogListView.as_view(), name='category'),
    

]