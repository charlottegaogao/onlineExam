from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('instantTest.views',
    url(r'^$','signin'),
    url(r'myTest/$','index'),
    url(r'^(?P<test_id>\d+)/(?P<question_id>\d+)/$', 'details'),
)
