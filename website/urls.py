from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'api.views.home', name='home'),
    url(r'^api/', include('api.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
