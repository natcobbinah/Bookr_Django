from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, views_api

router = DefaultRouter()
router.register(r'books', views_api.BookViewSet)
router.register(r'reviews', views_api.ReviewViewSet)

namespace = "user_reviews"
urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path('api/login', views_api.Login.as_view(), name='login'),
    path('books/', views.book_list, name="book_list"),
    path('book/<int:book_id>/', views.book_details, name="book_detail"),
    path('book-search/', views.book_search, name='book_search'),
    path('books/<int:book_pk>/reviews/new/',
         views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/',
         views.review_edit, name='review_edit'),
    path("publishers/<int:pk>/", views.publisher_edit, name="publisher_edit"),
    path("publishers/new/", views.publisher_edit, name='publisher_create'),
    path("books/<int:pk>/media/", views.book_media, name="book_media"),

]
