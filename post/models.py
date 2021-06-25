from django.db import models
from users.num_converter import NumConverter

class Pic(models.Model):
    
    name = models.CharField(max_length = 60, blank = False)
    description_sizes = models.TextField(blank = False, name = 'des_sizes', max_length = 360)
    camera = models.CharField(max_length = 60, blank = False)
    photographer = models.CharField(max_length = 60, blank = False)
    captured_time = models.DateField(blank = False)
    price = models.IntegerField(blank = False)
    pic_id = models.CharField(max_length = 60, blank = False)
    thumbnail = models.ImageField(upload_to = f'static/post/thumbnail/', null = False, blank = False)
    preview = models.ImageField(upload_to = f'static/post/preview/', null = False, blank = False)
    tags = models.CharField(max_length = 1000, blank = False)
    image_files = models.FileField(upload_to ='posts/ogFiles', null = True, blank = False)


    def price_view(self):
        return NumConverter(self.price)