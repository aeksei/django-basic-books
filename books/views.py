from datetime import datetime
from random import choice, randint

from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from django.shortcuts import render

from .models import books


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


def books_list(request: HttpRequest):
    query_author = request.GET.get("author")
    if query_author:
        books_list = [book for book in books if book['author'] == query_author]
        return JsonResponse(books_list, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})

    return JsonResponse(books, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


def random_book(request):
    book = choice(books)
    return JsonResponse(book, json_dumps_params={"ensure_ascii": False, "indent": 4})


def randon_book_with_missing(request):
    id_ = randint(0, 10)
    book = get_object_or_404(books, id_)
    return JsonResponse(book, json_dumps_params={"ensure_ascii": False, "indent": 4})


def get_path(request, sub_path_1):
    return HttpResponse(f"значение")


def get_book_detail(request, book_id: int):
    return JsonResponse(
        get_object_or_404(books, book_id),
        json_dumps_params={"ensure_ascii": False, "indent": 4}
    )


def home(request):
    context = {
        "books_list": books
    }
    return render(request, "books/home.html", context=context)


def about(request):
    return render(request, "books/about.html")
