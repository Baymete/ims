from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ims.views.home', name='home'),
    # url(r'^ims/', include('ims.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^inventory/', include('inventory.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'inventory.views.main', name='main'),
)
