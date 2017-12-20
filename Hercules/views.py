from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django_datatables_view.base_datatable_view import BaseDatatableView

from django_tables2.export.views import ExportMixin
from django_tables2_reports.views import ReportTableView
import djqscsv

from .models import Hercules
from .tables import HerculesTable
from .filters import HerculesFilter
# Create your views here.

class FilteredHercluesListView(SingleTableMixin,FilterView):
    table_class = HerculesTable
    model = Hercules    
    filterset_class = HerculesFilter
    table_pagination = {'per_page': 3}
    template_name = 'Hercules/bootstrap_template.html'

def HerculesList(request):
    filter = HerculesFilter(request.GET, queryset=Hercules.objects.all())
    return render(request, 'Hercules/asset_filter.html', {'filter': filter})
 
    

def get_csv(request):
    qs = Hercules.objects.all()
    return djqscsv.render_to_csv_response(qs)