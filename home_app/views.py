from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Visitor

# CSRF token endpoint
def get_csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})

@csrf_exempt  # Temporary for debugging, later use proper CSRF handling
def visitor_submission(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name", "")
            email = data.get("email", "")
            purpose = data.get("purpose", "")

            if not name or not email or not purpose:
                return JsonResponse({"error": "All fields are required"}, status=400)

            visitor = Visitor(name=name, email=email, purpose=purpose)
            visitor.save()

            return JsonResponse({"message": "Visitor data saved successfully"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)
