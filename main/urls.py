from django.urls import path
from .views import *
# from .view import
# here in this web app we dont actually use this url as an include and we 
# set these pkath directly in the main url file
urlpatterns = [
    path('', indexPageView,name = "index_page"),
    path('<str:pic>', indexPageView,name = "index_page")
]
