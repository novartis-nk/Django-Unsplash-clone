from django.urls import path
from .views import singlePostView

urlpatterns = [
	path('preview/<pic_id>', singlePostView, name = 'preview'),
]  
