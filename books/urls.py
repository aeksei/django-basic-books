from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('books_list/', views.books_list, name="book-list"),
    path('random_book/', views.random_book),
    path('randon_book_with_missing/', views.randon_book_with_missing),
    path('custom_path/<str:sub_path_1>/', views.get_path),
    path('books/<int:book_id>/', views.get_book_detail),
    path('category/<slug:category_slug>/books/',
         views.category_books,
         name="category-books"),
]
