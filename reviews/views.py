from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    """  name = request.GET.get("name") or "world"
     return HttpResponse(f"Hello, {name}!") """
    name = "world"
    return render(request, "base.html", {
        "name": name
    })


def searchbook(request):
    book_name = request.GET.get("search") or "no search query"
    return render(request, "searches/searchbooks.html", {
        "book_name": book_name
    })
