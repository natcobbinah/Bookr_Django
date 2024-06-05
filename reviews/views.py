from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review, Contributor, Publisher
from .utils import average_rating
from .forms import SearchForm, PublisherForm, ReviewForm
from django.contrib import messages
from django.utils import timezone


# Create your views here.


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({
            'book': book,
            'book_rating': book_rating,
            'number_of_reviews': number_of_reviews
        })

    context = {
        'book_list': book_list
    }
    return render(request, 'reviews/books_list.html', context)


def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {
            "book": book,
            "book_rating": book_rating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "reviews": None
        }
    return render(request, 'reviews/book_details.html', context)


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()

    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            fname_contributors = Contributor.objects.filter(
                first_names__icontains=search)

            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

            lname_contributors = Contributor.objects.filter(
                last_names__icontains=search)

            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)
    return render(request,
                  "search/search-results.html", {
                      "form": form,
                      "search_text": search_text,
                      "books": books
                  })


def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)

        if form.is_valid():
            updated_publisher = form.save()

            if publisher is None:
                messages.success(request,
                                 f"Publisher {updated_publisher} was created")
            else:
                messages.success(request,
                                 f"Publisher {updated_publisher} was updated")
            return redirect("publisher_edit", updated_publisher.pk)

    form = PublisherForm(instance=publisher)

    return render(request, "edit/instance-form.html", {
        "form": form,
        "instance": publisher,
        "model_type": "Publisher"
    })


def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)

    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            updated_review = form.save(commit=False)
            updated_review.book = book

            if review is None:
                messages.success(
                    request, f"Review for {book} created.")
            else:
                updated_review.date_edited = timezone.now()
                messages.success(
                    request, f"Review for {book} updated"
                )

            updated_review.save()
            return redirect("book_detail", book.pk)
    form = ReviewForm(instance=review)

    return render(request, "edit/instance-form.html", {
        "form": form,
        "instance": review,
        "model_type": "Review",
        "related_model_type": "Book",
        "related_instance": book,
    })
