from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib import messages, auth
from django.conf import settings
from django.contrib.auth.decorators import login_required
from models import Book, Comment
from forms import BookForm, CommentForm
from haystack.query import SearchQuerySet

import logging
logger = logging.getLogger(__name__)

# Create your views here.
def books(request):
	book_list = Book.objects.all()
	paginator = Paginator(book_list, 4)
	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)
	args = {}
	args['books'] = books
	return render(request, 'books.html', args)

def book(request, book_id=1):
	args = {}
	args['book'] = Book.objects.get(id=book_id)
	return render(request, 'book.html', args)

@login_required
def create(request):
	if request.method == 'POST':
		form = BookForm(request.POST, request.FILES)
		if form.is_valid:
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Your book was added!')
			return HttpResponseRedirect('/')
	else:
		form = BookForm()
	args = {}
	#args.update(csrf(request))
	args['form'] = form
	return render(request, 'create_book.html', args)


@login_required
def edit(request, book_id):
	b = Book.objects.get(id=book_id)
	if request.method == 'POST':
		form = BookForm(request.POST, request.FILES)
		if form.is_valid:
			c = form.save(commit=False)
			c.book = b
			c.save()
			messages.add_message(request, messages.SUCCESS, 'Your book was edited!')
			return HttpResponseRedirect('/books/get/%s' % book_id)
	else:
		form = BookForm()
	args = {}
	args['form'] = form
	return render(request, 'create_book.html', args)

@login_required
def delete(request, book_id):
	b = Book.objects.get(id=book_id)
	b.delete()
	return HttpResponseRedirect('/')


def like_book(request, book_id):
	if book_id:
		b = Book.objects.get(id=book_id)
		b.likes += 1
		b.save()
	return HttpResponseRedirect('/books/get/%s'% book_id)

@login_required
def add_comment(request, book_id):
	book = Book.objects.get(id=book_id)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			com = form.save(commit=False)
			com.pub_date = timezone.now()
			com.book = book
			com.save()
			messages.add_message(request, messages.SUCCESS, 'Your comment was added!')
			return HttpResponseRedirect('/books/get/%s'% book_id)
	else:
		form = CommentForm()
	user = auth.get_user(request).username
	args = {}
	args['user'] = user
	#args.update(csrf(request))
	args['form'] = form
	args['book'] = book
	return render(request, 'add_com.html', args)


@login_required
def delete_comment(request, com_id):
	comment = Comment.objects.get(id=com_id)
	book_id = comment.book.id
	comment.delete()
	messages.add_message(request, settings.DELETE_MESSAGE, 'Your comment was delete!')
	return HttpResponseRedirect('/books/get/%s'% book_id)


def search_titles(request):
	books = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text',''))
	args = {}
	args['books'] = books
	return render(request, 'ajax_search.html', args)
