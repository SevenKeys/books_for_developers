from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Book

class BookResource(ModelResource):
	class Meta:
		queryset = Book.objects.all()
		resource_name = 'book'
		foltering = {'title':ALL}