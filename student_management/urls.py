from django.conf.urls import patterns, include, url
from django.contrib import admin

from management.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'student_management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search/st/id', search_st_id),
    url(r'^search/st/name', search_st_name),
    url(r'^search/st/major', search_st_major),

    url(r'^st/create/', st_create),
    url(r'^admin/', include(admin.site.urls)),
)

