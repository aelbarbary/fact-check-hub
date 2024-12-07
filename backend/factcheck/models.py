from django.db import models

# create a new model for political facts. each fact should have text, created at and status. status could be one of following [verified, pending and false]

class Fact(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('verified', 'Verified'),
        ('pending', 'Pending'),
        ('false', 'False'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    source_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.text[:20]}"
