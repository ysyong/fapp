from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','polls.views.index'),
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
