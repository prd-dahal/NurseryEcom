from django.urls import path
from . import views 

app_name = 'CustomerLogin'
urlpatterns = [
    path('register', views.register, name='customerRegister'),
    path('dashboard', views.dashboard, name ='customerDashboard'),
    path('login', views.login, name='customerLogin'),
    path('logout', views.logout_request, name='customerLogout')
  
]