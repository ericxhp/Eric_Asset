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
import xlrd

from .models import Hercules
from .tables import HerculesTable
from .filters import HerculesFilter
# Create your views here.

from .forms import SourcePathForm

class FilteredHercluesListView(SingleTableMixin,FilterView):
    table_class = HerculesTable
    model = Hercules    
    filterset_class = HerculesFilter
    table_pagination = {'per_page': 25}
    template_name = 'Hercules/bootstrap_template.html'

def HerculesList(request):
    table = HerculesTable(Hercules.objects.all())
    return render(request, 'Hercules/bootstrap_table.html', {'table': table})

 
def get_csv(request):
    qs = Hercules.objects.all()
    return djqscsv.render_to_csv_response(qs)

def readExcelData(path):
    STATUS_PASS = 0
    STATUS_FAIL = 1
    try:
        data = xlrd.open_workbook(path)
        table = data.sheets()[0]
        rwo_num = table.nrows
        print rwo_num
        for i in range(1,rwo_num):
            data = table.row_values(i)
            cdata=[]
            for item in data:
                cdata.append(str(item))
             
            tmp = Hercules.objects.create()
            tmp.asset_num =  cdata[0]
            tmp.desciption = cdata[1]
            tmp.serial_num = cdata[2]
            tmp.asset_type = cdata[3]
            tmp.location = cdata[4]
            tmp.status = cdata[5]
            tmp.owner = cdata[6]
            tmp.assignee = cdata[7]
            tmp.order_num = cdata[8]
            tmp.note = cdata[9]
            tmp.save()
    except:
        print "Import data fail"
        return STATUS_FAIL
    else:
        print "Import data PASS"
        return STATUS_PASS
        

def import_db(request):
    status = 0
    if request.method == 'POST':
        # Form was submitted
        form = SourcePathForm(request.POST)
        if form.is_valid():
            path = form.cleaned_data
            status = readExcelData(path['path'])
            print status
    else:
        form = SourcePathForm()
    return render(request, 'Hercules/Path.html', {'form': form,'status':status})


