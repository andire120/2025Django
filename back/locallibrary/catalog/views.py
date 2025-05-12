import datetime
from django.shortcuts import render
from django.views import generic

from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count # 책 오브젝트 모두 가져옴
    num_instances = BookInstance.objects.all().count() #책 복사본 오브젝트 가져옴

    #대출 가능한 책의 갯수 카운트
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    #작가를 모두 가져오고 갯수 카운트
    num_authors = Author.objects.count()

    #session을 사용해서 방문자수 받아오기
    num_visits =  request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'num_visits' : num_visits,
    }

    #index.html에 변수를 render한다.
    return render(request, 'index.html', context=context)

#가져온 책들을 ListView 형태로 보여줌
class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'  # ← 이 경로로 직접 지정

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'