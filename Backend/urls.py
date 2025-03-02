
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('home_app.urls')),  # Include app URLs under `/api/`
    path('', include('home_app.urls')),  # Include home_app's URLs for `/`
]