from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    review_text = models.TextField()

    def __str__(self):
        return self.review_text
    