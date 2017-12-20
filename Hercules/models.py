from __future__ import unicode_literals

from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

STATUS_CHOICES = (
    ('in stock', 'InStock'),
    ('in use', 'InUse'),
    ('in repair', 'InRepair'),
    ('broken', 'Broken'),
)


class Hercules(models.Model):

    asset_num =  models.CharField(max_length=250, verbose_name='asset number')
    desciption = models.CharField(max_length=250, verbose_name='description')
    serial_num = models.CharField(max_length=250, verbose_name='serial number')    
    asset_type = models.CharField(max_length=250, verbose_name='type')
    location = models.CharField(max_length=250, verbose_name='location')
    status = models.CharField(max_length=10, verbose_name='status',
                                choices=STATUS_CHOICES,
                                default='in stock')
    owner = models.CharField(max_length=250, verbose_name='owner')
    assignee = models.CharField(max_length=250, verbose_name='assignee')
    order_num = models.CharField(max_length=250, verbose_name='order num')
    note = models.TextField()
    recorded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()