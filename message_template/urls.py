from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'message_template.views.show_all', name='message_template_show_all'),
)
