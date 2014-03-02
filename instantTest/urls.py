from django.conf.urls import patterns, url

urlpatterns = patterns('instantTest.views',
    url(r'^$','signin'),
    url(r'myTest/$','index'),
    url(r'^(?P<test_id>\d+)/(?P<question_id>\d+)/$', 'details'),
    
)