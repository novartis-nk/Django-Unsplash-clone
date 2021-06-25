import django_filters
from django_filters import CharFilter
from post.models import Pic

class PicFilter(django_filters.FilterSet):
    tags = CharFilter(field_name = 'tags', lookup_expr = 'icontains')


    class Meta :
        model = Pic
        fields = ['tags']