from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home'),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="auth_login"),
    #url(r'^accounts/profile/$', redirect, {'url': '/'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name="auth_logout"),
    url(r'^accounts/', include('registration.urls')),

    url(r'^targets/', include('targets.urls')),
    url(r'^pipelines/', include('pipelines.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
