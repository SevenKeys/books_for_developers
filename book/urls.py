from django.conf.urls import url, patterns, include
from api import BookResource
from it_book.forms import ContactForm1, ContactForm2, ContactForm3
from it_book.views import ContactWizard

book_resource = BookResource()

urlpatterns = patterns('',
	url(r'^get/(?P<book_id>\d+)/$', 'book.views.book', name='book'),
	url(r'^create/$', 'book.views.create', name='create'),
	url(r'^edit/(?P<book_id>\d+)$', 'book.views.edit', name='edit'),
	url(r'^delete/(?P<book_id>\d+)$', 'book.views.delete', name='delete'),
	url(r'^like/(?P<book_id>\d+)/$', 'book.views.like_book', name='like'),
	url(r'^add_comment/(?P<book_id>\d+)/$', 'book.views.add_comment', name='add_com'),
	url(r'^delete_comment/(?P<com_id>\d+)/$', 'book.views.delete_comment', name='delete_comment'),
	url(r'^search/$', 'book.views.search_titles', name='search'),
	url(r'^api/', include(book_resource.urls)),
	url(r'^contacts/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
	)