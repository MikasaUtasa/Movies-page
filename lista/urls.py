from django.urls import path, include
from . import views

from .models import Film

urlpatterns = [
    path('' , views.main, name='main'),
    path('list/' , views.list, name='list'),
    path('user/', views.user, name='user_panel'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('<int:movie_id>/',views.detail,name='detail'),
    path('director/<int:director_id>/',views.director_list, name='director'),
    path('cart/add/<int:movie_id>/', views.cart_add, name='add_to_cart'),
    path('cart/delete/<int:movie_id>', views.cart_delete, name='delete'),
    path('list/search/', views.Search, name="search_results"),

]
