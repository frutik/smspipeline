from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'targets.views.show_all', name='targets_show_all'),
    url(r'add/$', 'targets.views.add', name='targets_add'),
    url(r'change_many/$', 'targets.views.change_many', name='targets_change_many'),
)
