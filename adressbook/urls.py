from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'adressbook.views.show_all', name='adressbook_show_all'),
)
