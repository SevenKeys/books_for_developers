from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
#from django.core.context_processors import csrf
from forms import MyRegistrationForm
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from notification.models import Notification
import logging

logr = logging.getLogger(__name__)

def login(request):
	context = {}
	context.update(csrf(request))
	return render(request, 'login.html', context)

def auth_view(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)# enter user
			return HttpResponseRedirect('/accounts/loggedin/')
		else:
			return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	n = Notification.objects.filter(user=request.user, viewed=False)
	args = {}
	args['full_name'] = request.user.username # to know name while registration
	args['notifications'] = n
	return render(request, 'loggedin.html', args)

def invalid(request):
	return render(request, 'invalid.html')

def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect('/accounts/register_success')
	args = {}
	#args.update(csrf(request))
	args['form'] = MyRegistrationForm()
	return render(request,'register.html', args)	

def register_success(request):
	user = auth.get_user(request).username
	args = {}
	args['user'] = user
	return render(request,'register_success.html', args)

class ContactWizard(SessionWizardView):
    template_name = "contact_form.html"
    
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        
        return render_to_response('done.html')
    
    
def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    
    logr.debug(form_data[0]['subject'])
    logr.debug(form_data[1]['sender'])
    logr.debug(form_data[2]['message'])
    
    send_mail(form_data[0]['subject'], 
              form_data[2]['message'], 
              form_data[1]['sender'],# from whom will be sent email
              ['tsmyh@mail.ru'], # email to whom will be sent mail
              fail_silently=False)
    
    return form_data

def contacts(request):
	return render(request, 'contacts.html')
