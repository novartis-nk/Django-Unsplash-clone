from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm 
from .models import Order  
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user ,authenticated_user
from .num_converter import NumConverter


# registeration view function
@unauthenticated_user
def registerationPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateUserForm()
    context = {'form': form,}
    return render(request, 'users/registeration_page.html', context)


# login view function
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request ,user)
            return redirect('/')
        else:
            redirect('users/login_page.html')                                       #should be changed
    return render(request, 'users/login_page.html')


# logout function that redirects you to the main page when you logout
def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


# shopping card view that loops through the user.queue list and get the photos
@authenticated_user
def shoppingCard(request):
    final_price = 0
    user = request.user
    orders = Order.objects.filter(user = user)
    count = orders.count()
    for order in orders:
        final_price +=order.pic.price 
    view_final_price =  NumConverter(final_price)
    context = {
    'orders': orders,
    'count':count,
    'final_price':view_final_price,
    }
    return render(request, 'users/fa-purchase_history.html', context)

@authenticated_user
def deleteOrder(request, order_id):
    order = Order.objects.get(pk=order_id)
    user = request.user
    if order.user == user:
        order.delete()
        return redirect('shopping_card')
#@authenticated_user
#def profileStatus(request): this is for when we needed profile 
