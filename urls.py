from django.conf.urls.defaults import patterns, include, url
from django.shortcuts import redirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="auth_login"),
    #url(r'^accounts/profile/$', redirect, {'url': '/'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name="auth_logout"),
    url(r'^accounts/', include('registration.urls')),

    url(r'^targets/', include('targets.urls')),
    url(r'^pipelines/', include('pipelines.urls')),
    
    # url(r'^django_tests/', include('django_tests.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
