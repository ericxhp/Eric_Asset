"""Asset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Hercules.views import FilteredHercluesListView,get_csv,HerculesList,import_db

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hercules/$', FilteredHercluesListView.as_view(), name='Hercules'),
    url(r'^test/$',get_csv , name='export'),
    url(r'^filter/$',HerculesList , name='filter'),
    url(r'^import/$',import_db, name='import'),
    
]
