books_for_developers
====================

Books for developers
In this app you cah add and remove books with pictures as well comments. Rights are reserverd for registered users.
Used technologies: "south" for changes in database, search system with "Ajax", "whoosh" and "haystack", django-tastypie for watching site in json or html formats. Errors are sent to file. It is posiible to send messages to admin email. For design used bootstrap. Also added paypal button for buying books.

You should enter(UNIX OS):
 
$ virtualenv env

$ cd env

$ git clone https://www.github.com/SevenKeys/books_for_developers.git

$ source bin/activate

$ cd books_for_developers

$ pip install -r requirements.txt

$ python manage.py runserver
