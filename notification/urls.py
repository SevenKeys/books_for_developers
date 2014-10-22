from django.conf.urls import patterns, url, include

urlpatterns = patterns('notification.views',
	url(r'^show/(?P<notification_id>\d+)/$', 'notification_show', name='notification_show'),
	url(r'^delete/(?P<notification_id>\d+)/$', 'notification_delete', name='notification_delete'),

)