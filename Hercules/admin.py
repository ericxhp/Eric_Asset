from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from .models import Hercules

#Control admin style
class HerculesAdmin(admin.ModelAdmin):
    
    list_display = ('asset_num', 'desciption', 'serial_num', 'asset_type',
                    'location','status','owner','assignee','order_num','note')
    list_filter = ('asset_type','status', 'owner', 'assignee')
    search_fields = ('asset_type','status', 'owner', 'assignee')

class HerculesHistoryAdmin(SimpleHistoryAdmin):
    list_display = ('asset_num', 'desciption', 'serial_num', 'asset_type',
                    'location','status','owner','assignee','order_num','note')
    history_list_display = ('asset_num', 'desciption', 'serial_num', 'asset_type',
                    'location','status','owner','assignee','order_num','note')
    list_filter = ('asset_type','status', 'owner', 'assignee')
    search_fields = ('asset_type','status', 'owner', 'assignee')

# Register your models here.
admin.site.register(Hercules,HerculesHistoryAdmin)