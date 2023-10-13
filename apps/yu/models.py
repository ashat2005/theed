from django.db import models


class Mail(models.Model):
    video_url = models.URLField(max_length=200)

    email = models.EmailField()

    def __str__(self):
        return f"Conversion Request ({self.id}) - Email: {self.email}"
