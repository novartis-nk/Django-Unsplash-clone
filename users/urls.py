from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerationPage),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('shopping_card', views.shoppingCard, name='shopping_card'),
    path('delete_order/<order_id>', views.deleteOrder, name='delete_order'),
    #path('profile/', views.profileStatus, name='profile'), for when we needed profile 

]
