from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'targets.views.show_all', name='targets_show_all'),
)
