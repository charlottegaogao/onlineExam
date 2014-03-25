from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from instantTest import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^instantTest/', include('instantTest.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^choosePoint/$', views.list_point),
    #url(r'^allocatepoint/$',TemplateView.as_view(template_name="allocatepoint.html")),
    url(r'^result/$', views.random_produce),
)
