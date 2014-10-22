from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'book.views.books', name='books'),
    url(r'^books/', include('book.urls')),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^notification/', include('notification.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # accounts urls
    url(r'^accounts/login/$','it_book.views.login', name='login'),
    url(r'^accounts/auth/$','it_book.views.auth_view', name='auth'),
    url(r'^accounts/logout/$','it_book.views.logout', name='logout'),
    url(r'^accounts/loggedin/$','it_book.views.loggedin', name='loggedin'),
    url(r'^accounts/invalid/$','it_book.views.invalid', name='invalid'),
    url(r'^accounts/register/$','it_book.views.register_user', name='register'),
    url(r'^accounts/register_success/$','it_book.views.register_success', name='invalid'),
    url(r'^contacts/$', 'it_book.views.contacts', name='contacts'),
    url(r'^search/', include('haystack.urls')),
)
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
		                  document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
		                  document_root=settings.MEDIA_ROOT)
