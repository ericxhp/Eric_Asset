'''
Created on Dec 19, 2017

@author: ericxu
'''
import django_filters

from django_filters import FilterSet

from .models import Hercules
from .models import STATUS_CHOICES

FILTER_STATUS_CHOICE = list(STATUS_CHOICES)


class HerculesFilter(FilterSet):
    status = django_filters.ChoiceFilter(choices=FILTER_STATUS_CHOICE)

    class Meta:
        model = Hercules
        fields = {
            'asset_type': ['contains'],
            'owner': ['contains'],
            'assignee': ['contains'],
        }

    def __init__(self, *args, **kwargs):
        super(HerculesFilter, self).__init__(*args, **kwargs)
        self.filters['status'].extra.update(
            {'empty_label': u'All Status'})
