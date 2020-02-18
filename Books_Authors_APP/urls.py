from django.urls import path
from . import views

urlpatterns = [
    path('authors/addbook/<int:num>', views.add_toAuthor),
    path('books/addauthor/<int:num>', views.add_toBook),
    path('authors/add', views.addAuthor),
    path('books/add', views.addBook),
    path('authors/<int:num>', views.authorDetails),
    path('books/<int:num>', views.bookDetails),
    path('authors', views.showAuthors),
    path('', views.index),
]