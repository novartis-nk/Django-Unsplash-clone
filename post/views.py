from django.shortcuts import render
from .models import Pic
def singlePostView(request, pic_id = None):
	order_count = 0
	pic = Pic.objects.get(id = pic_id)
	print(pic)

	context = {
	'pic':pic,
	}
	return render(request,"post/single_post_view.html", context)
