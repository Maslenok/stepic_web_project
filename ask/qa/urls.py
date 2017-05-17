from django.conf.urls import url
from django.contrib import admin
from qa.views import test,error404

urlpatterns = [
    url(r'^question/(?P<num>\d+)/$', test),
    url(r'^login/', test),
    url(r'^singup/', test),
    url(r'^ask/', test),
    url(r'^new/', test),
    url(r'^popular/', test),
    url(r'^$', test),
	url(r'^/$', error404),
]
