from django.conf.urls import patterns, include, url
from django.contrib import admin
from tournaments import urls as tournaments_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nctta_savethetrees.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(tournaments_urls)),

    url(r'^admin/', include(admin.site.urls)),
)
