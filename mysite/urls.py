from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^rallybench/', include('rallybench.urls')),
    url(r'^poll/', include('poll.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

