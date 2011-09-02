from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'targets.views.show_all', name='targets_show_all'),
    url(r'add_twitter/$', 'targets.views.add_twitter', name='targets_add_twitter'),
)
