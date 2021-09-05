from django.urls import path
from . import views 

app_name = 'Shop'
urlpatterns = [
    path('', views.index, name='shopIndex'),
    path('view/<slug:category>', views.filter, name='filter'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cartDisplay', views.display_cart, name='display_cart'),
    path('updateCart', views.update_cart, name='update_cart'),
    path('deleteCart', views.delete_cart, name='delete_cart'),
    path('search', views.search, name= 'search_product')
]