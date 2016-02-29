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

    url(r'sc/add', sc_add),
    url(r'sc/search', sc_search),
    url(r'sc/average', sc_average),

    url(r'my_teachers', my_teachers),
    
    url(r'warn', warn),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index', sc_add_auto),
)

