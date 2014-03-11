<<<<<<< HEAD
from django.conf.urls import patterns, url

urlpatterns = patterns('instantTest.views',
=======
from django.conf.urls import patterns, include, url



urlpatterns = patterns('instantTest.views',
    # Examples:
    # url(r'^$', 'onlineTest.views.home', name='home'),
    # url(r'^onlineTest/', include('onlineTest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
>>>>>>> master
    url(r'^$','signin'),
    url(r'myTest/$','index'),
    url(r'^(?P<test_id>\d+)/(?P<question_id>\d+)/$', 'details'),
    
<<<<<<< HEAD
)
=======
)
>>>>>>> master
