from django.urls import path
from . import views 

app_name = 'BasicNavs'
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('contactUs', views.contactUs, name='contactUs')
]