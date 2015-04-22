from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^client/$',views.index,name='index'),
	#url(r'^client/(?P<client_id>[0-9]+)/$',views.client,name='client'),
	
	url(r'^client/(?P<client_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'^client/addclient/$',views.addclient,name='addclient'),
	url(r'^client/(?P<client_id>[0-9]+)/addproject/$',views.addproject,name='addproject'),
	url(r'^client/(?P<client_id>[0-9]+)/projectdetails/(?P<project_id>[0-9]+)/$',views.projectdetails,name='projectdetails'),
	url(r'^client/(?P<client_id>[0-9]+)/project/(?P<project_id>[0-9]+)/report/$',views.report,name='report'),
	]
