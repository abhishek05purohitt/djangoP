from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader
from django.shortcuts import render
from django.http import Http404


# Create your views here.
 
def index(request):
    all_books = Book.objects.all()

    context = {
       'all_books': all_books
    }
    return render(request,'books/index.html',context)

def detail(request,book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('this book does not exist')
    return render(request,'books/detail.html',{'book':book})
  