from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Notification

# Create your views here.
def notification_show(request, notification_id):
	n = Notification.objects.get(id=notification_id)
	args = {}
	args['notification'] = n
	return render(request, 'notification.html', args)

def notification_delete(request, notification_id):
	n = Notification.objects.get(id=notification_id)
	n.viewed = True
	n.save()
	return HttpResponseRedirect('/accounts/loggedin')