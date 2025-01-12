from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Post modeli
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    summary = models.CharField(max_length=500, blank=True, null=True)  # summary maydoni qo'shildi
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Post uchun URL manzilini qaytaruvchi metod
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

