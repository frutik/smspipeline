from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'pipelines.views.show_all', name='pipelines_show_all'),
    url(r'add/$', 'pipelines.views.add', name='pipelines_add'),
    url(r'log/$', 'pipelines.views.execution_log', name='pipelines_execution_log'),
)
