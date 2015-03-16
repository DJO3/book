from django.shortcuts import render
from library.models import Author, Book
from library.forms import AuthorForm, BookForm


def book(request, book_name_slug):
    context_dict = {'book_name_slug': book_name_slug}

    try:
        book = Book.objects.get(slug=book_name_slug)
        context_dict['book_name'] = book.name

        context_dict['book'] = book
        author = Author.objects.filter(category=book)
        context_dict['author'] = author

    except Book.DoesNotExist:
        pass
    return render(request, 'library/book.html', context_dict)


def add_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return Book(request)
        else:
            print form.errors

    else:
        form = BookForm()

    return render(request, 'library/add_book.html', {'form': form})

