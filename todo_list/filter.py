import django_filters
from .models import List
from django_filters import CharFilter


class OrderFilter(django_filters.FilterSet):
    item = CharFilter(Filed_name='item', lookup_expr='icontains')
    
    class meta:
        model = List
        fields = '__all__'