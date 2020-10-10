from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='users/uploads')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    garden = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            if img.height > 600 or img.width > 600:
                max_size = (600, 600)
                img.thumbnail(max_size, Image.ANTIALIAS)
                img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})