from django.urls import path
from . import views

namespace = "user_reviews"
urlpatterns = [
    path('', views.index, name='index'),
    path('book-search/', views.searchbook, name='searchbook'),
]
