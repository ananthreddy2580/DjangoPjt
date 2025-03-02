from django.urls import path
from django.http import HttpResponse
from .views import visitor_submission, get_csrf_token,home

# Simple function to return a response for "/"

urlpatterns = [
    path('', home, name='home'),  # Add this line for the root URL
    path('visitors/', visitor_submission, name='visitor_submission'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
]
