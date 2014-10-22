from django import forms
from models import Book, Comment
from django.utils import timezone

class BookForm(forms.ModelForm):

	class Meta:
		model = Book
		fields = ('title', 'author', 'description', 'pub_date', 'thumbnail')

class CommentForm(forms.ModelForm):
	pub_date = forms.DateTimeField(initial=timezone.now())

	class Meta:
		model = Comment
		fields = ('name', 'body', 'pub_date')