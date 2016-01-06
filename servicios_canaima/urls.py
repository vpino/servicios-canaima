from django.conf.urls import patterns, include, url
from django.contrib import admin
from info import api_01

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'servicios_canaima.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'info.views.homepage', name='homepage'),
    url(r'^generic/$', 'info.views.package_generic', name='generic'),
    url(r'^generic/create/$', 'info.views.generic_create', name='generic_create'),
    url(r'^generic/edit/(?P<package_id>\d+)/$', 'info.views.generic_edit', name='generic_edit'),
    url(r'^packages/genericedu/$', 'info.views.package_generic_edu', name='generic_edu'),
    url(r'^packages/genericedu/create/$', 'info.views.generic_edu_create', name='generic_edu_create'),
    url(r'^packages/genericedu/edit/(?P<package_id>\d+)/$', 'info.views.generic_edu_edit', name='generic_edu_edit'),
	url(r'^api/', view=include(api_01.urls)),
    url(r'^repositorios/$', 'info.views.repositorios_list', name='repositorios_list'),
    url(r'^repositorios/create/$', 'info.views.repositorios_create', name='repositorios_create'),
    url(r'^repositorios/edit/(?P<repositorio_id>\d+)/$', 'info.views.repositorios_edit', name='repositorios_edit'),
    url(r'^repositorios/delete/(?P<repositorio_id>\d+)/$', 'info.views.repositorios_delete', name='repositorios_delete'),

)
