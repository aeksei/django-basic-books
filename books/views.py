from datetime import datetime
from random import choice, randint

from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from django.shortcuts import render

from .models import books, categories_data


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
    context = {
        "categories": categories_data,
        "book": get_object_or_404(books, book_id),
    }

    return render(request, "books/book_detail.html", context=context)


def home(request):
    context = {
        "books_list": books,
        "categories": categories_data,
    }
    return render(request, "books/home.html", context=context)


def about(request):
    context = {
        "categories": categories_data,
    }
    return render(request, "books/about.html", context=context)


def category_books(request, category_slug: str):
    category_name = None
    for category in categories_data:
        if category["slug"] == category_slug:
            category_name = category["name"]

    books_list = [book for book in books if book['category'] == category_slug]

    context = {
        "books_list": books_list,
        "categories": categories_data,
        "category_name": category_name,
    }
    return render(request, "books/category_books.html", context=context)
