from django.urls import path
from . import views

namespace = "user_reviews"
urlpatterns = [
    path('books/', views.book_list, name="book_list"),
    path('book/<int:book_id>/', views.book_details, name="book-details"),
]
