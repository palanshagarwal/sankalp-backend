from django.conf.urls import patterns, include, url

from api import views

urlpatterns = patterns('',
    url(r'^events/',views.EventList.as_view()),
)
