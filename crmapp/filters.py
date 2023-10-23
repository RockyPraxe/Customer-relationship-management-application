import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


# OrderFilter defines filters for the Order model,
# allowing users to filter and query orders based on criteria such as
# date range and partial matching of the 'note' field.


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
