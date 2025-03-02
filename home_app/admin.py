from django.contrib import admin
from .models import Visitor  # Import your model

# Register the model to make it visible in the admin panel
admin.site.register(Visitor)
