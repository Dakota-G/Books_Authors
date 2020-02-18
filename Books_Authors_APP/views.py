from django.shortcuts import render, redirect
from .models import *

# GET REQUESTS:
def index(request):
    context = {
        'books': Book.objects.all() 
    }
    return render(request, 'index.html', context)

def showAuthors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def authorDetails(request, num):
    context = {
        'author': Author.objects.get(id = num),
        'books': Book.objects.all()
    }
    return render(request, 'authordetails.html', context)

def bookDetails(request, num):
    context = {
        'book': Book.objects.get(id = num),
        'authors': Author.objects.all()
    }
    return render(request, 'bookdetails.html', context)

# POST REQUEST:
def addBook(request):
    if request.method == 'POST':
        Book.objects.create(title = request.POST['title'])
    return redirect('/')

def addAuthor(request):
    if request.method == 'POST':
        Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'])
    return redirect('/authors')

def add_toBook(request, num):
    book = Book.objects.get(id = num)
    book.authors.add(Author.objects.get(id = request.POST['new_author_id']))
    book.save()
    return redirect('/')

def add_toAuthor(request, num):
    author = Author.objects.get(id = num)
    author.books.add(Book.objects.get(id = request.POST['new_book_id']))
    author.save()
    return redirect(f'/authors/{num}')
    