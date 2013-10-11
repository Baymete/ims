from django.conf.urls import patterns, url
from inventory import views

urlpatterns = patterns('',
        url(r'^itemhistory/(?P<id>\d+)/$', views.item_history, name='item_history'),
        url(r'^users/$', views.users, name='users'),
        url(r'^$', views.main, name='main'),
        )