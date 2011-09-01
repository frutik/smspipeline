from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'pipelines.views.show_all', name='pipelines_show_all'),
)
