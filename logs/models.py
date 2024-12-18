from django.db import models
from users.models import CustomUser

class Log(models.Model):
    CATEGORY_CHOICES = [
        ('INFO', 'Information'),
        ('ERROR', 'Error'),
        ('WARNING', 'Warning'),
    ]
    LEVEL_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='logs')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    message = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.message[:50]}"