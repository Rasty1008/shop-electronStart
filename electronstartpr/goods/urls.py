from django.urls import path

from goods import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('search/', views.catalog, name='search'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.catalog, name='category'),
    

]