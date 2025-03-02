from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    purpose = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-add timestamp

    def __str__(self):
        return self.name