from django.urls import path
from django.http import HttpResponse
from .views import visitor_submission, get_csrf_token

# Simple function to return a response for "/"
def home(request):
    return HttpResponse("Welcome to the Visitor API! Use /visitors/ to submit data.")

urlpatterns = [
    path('', home, name='home'),  # Add this to fix the 404 error
    path('visitors/', visitor_submission, name='visitor_submission'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
]
