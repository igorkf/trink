from django.db import models
from django.utils import timezone

# Create your models here.


class Link(models.Model):
    url = models.CharField(max_length=100)
    shortened_url = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now(), editable=False)
    # TODO: relation with User model
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.url
