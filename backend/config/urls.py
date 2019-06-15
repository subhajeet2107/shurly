from django.urls import path,re_path
from django.contrib import admin
from django.contrib.auth import logout

from django.conf.urls import include

from config.api import api
from apps.director.views import redirector



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),

    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('r/<short_url_hash>', redirector, name='redirector'),
]
