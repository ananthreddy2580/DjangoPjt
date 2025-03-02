from django.urls import path
from .views import visitor_submission,get_csrf_token

urlpatterns = [
    path('visitors/', visitor_submission, name='visitor_submission'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),

]
