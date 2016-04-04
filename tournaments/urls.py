from django.conf.urls import patterns, url

from tournaments import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
