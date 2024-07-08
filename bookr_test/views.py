from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def greeting_view(request):
    """Greet the user"""
    return HttpResponse("Hey there, welcom to Bookr, your one stop place \
                        to review books")


@login_required
def greeting_view_user(request):
    """Greeting view for the user"""
    user = request.user
    return HttpResponse(f"welcome to Bookr! {user}")
