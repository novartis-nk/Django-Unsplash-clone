from django.db import models
from post.models import Pic
from django.contrib.auth.models import User

class Order(models.Model):
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    pic     = models.ForeignKey(Pic,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default = False, blank = False)
    ref_id  = models.CharField(max_length = 120, default = "")

    def get_ref_id(self):
        return ref_id

    def change_ref_id(self, ref):
        self.ref_id = ref 