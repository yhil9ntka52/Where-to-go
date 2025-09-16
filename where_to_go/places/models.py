from django.db import models

class Place(models.Model):
    user_session = models.CharField(max_length=64)
    name = models.CharField(max_length=100)
    description = models.TextField()
    place_type = models.CharField(max_length=50)
    location = models.CharField(max_length=255, blank=True)
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo_filename = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
