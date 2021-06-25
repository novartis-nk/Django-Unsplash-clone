from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path('', indexPageView,name = "index_page"),
    path('<str:pic>', indexPageView,name = "index_page"),
    path('authenticate/', include('users.urls')),
    #path('order/', include('order.urls')),
    path('post/', include('post.urls')),
    path('admin/', admin.site.urls),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
