'''
Created on Dec 19, 2017

@author: ericxu
'''
import django_tables2 as tables

from .models import Hercules

class SummingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return sum(bound_column.accessor.resolve(row) for row in table.data)
    
class HerculesTable(tables.Table):
    class Meta:
        model = Hercules
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        template = 'django_tables2/bootstrap.html'