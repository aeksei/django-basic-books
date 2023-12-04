from datetime import datetime
from random import choice, randint

from django.http import HttpResponse, HttpRequest, JsonResponse, Http404


books = [
    {"id": 1, "title": "Книга 1", "author": "Автор 1"},
    {"id": 2, "title": "Книга 2", "author": "Автор 2"},
    # ... другие книги
]


def get_object_or_404(all_books: list, id_: int) -> dict:
    for book in all_books:
        if book["id"] == id_:
            return book

    raise Http404


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"<h1>Добро пожаловать в библиотеку!!!</h1>")


def about_handler(request):
    now = datetime.now()
    return HttpResponse(f"Сайт разработан в {now.year}.")


def books_list(request):
    return JsonResponse(books, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


def random_book(request):
    book = choice(books)
    return JsonResponse(book, json_dumps_params={"ensure_ascii": False, "indent": 4})


def randon_book_with_missing(request):
    id_ = randint(0, 10)
    book = get_object_or_404(books, id_)
    return JsonResponse(book, json_dumps_params={"ensure_ascii": False, "indent": 4})