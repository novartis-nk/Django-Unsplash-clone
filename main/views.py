from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator , EmptyPage
from .filters import PicFilter
from post.models import Pic
from users.models import Order

# from django.contrib.auth.decorators import login_required
# Create your views here.

def indexPageView(request, pic=None):
    # we asign the order counter as 0 until  we know that user is authanticated  
  # this is just only for the viewing the search bar and preventing redandency BTW IK it's not the best way
    order_count = 0
    if request.user.is_authenticated:
        if pic:
            user = request.user
            print(user, "and this is the picture object", pic)
            d_pic = Pic.objects.get(pic_id = pic)
            existed_obj = len(Order.objects.filter(user= user, pic = d_pic))
            if existed_obj == 0 :
                Order.objects.create(user = user, pic = d_pic)
                print(Order.objects.all())

            else:
               print("THIS OBJECT BEEN ADDED TO THE DATA BASE BEFORE")

        order_count = len(Order.objects.filter(user = request.user))
    pics = Pic.objects.all()
    myFilter = PicFilter(request.GET, queryset=pics)
    pics = myFilter.qs
    #filtered_pics = PicFilter(request.GET,queryset = pics )
    paginated_objects = Paginator(pics, 12)
    page_number = request.GET.get('page',1)
    try:
        paginated_pic = paginated_objects.page(page_number)
        print(paginated_pic, 'here we found the requested page ')
    except EmptyPage:
        paginated_pic = paginated_objects.page(1)
        print(paginated_pic, 'here the page that been requested is unvalid ')
    count = len(paginated_pic.object_list) + 3
    pics_range = range(3, count)
    zipped_data1 = zip(paginated_pic, pics_range)
    zipped_data2 = zip(paginated_pic, pics_range)
    zipped_data3 = zip(paginated_pic, pics_range)
    context = {
    'zipped_data1': zipped_data1,
    'zipped_data2': zipped_data2,
    'zipped_data3': zipped_data3,
    'order_count': order_count,
    'page':paginated_pic, 
    'myFilter':myFilter,
    }
    return render(request, 'main/main_page.html', context)

