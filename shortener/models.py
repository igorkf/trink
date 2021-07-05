import string

from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

EXPIRATION_DAYS = 7
DOMAIN = 'https://trink.com.br/'


def timezone_delta():
    return timezone.now() + timezone.timedelta(days=EXPIRATION_DAYS)


class Link(models.Model):
    url = models.CharField(max_length=200)
    shortened_url = models.CharField(max_length=100, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_by',
        db_column='created_by'
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    expires_at = models.DateTimeField(
        default=timezone_delta, editable=False)

    def encode(self, id_):
        '''62 chars encoder'''
        characters = string.digits + string.ascii_letters
        base = len(characters)

        result = []
        while id_ > 0:
            val = id_ % base
            result.append(characters[val])
            id_ = id_ // base

        return DOMAIN + ''.join(result[::-1])

    def save(self, *args, **kwargs):
        id_digits = int(1e8)

        # get last id first
        last_link = Link.objects.last()
        try:
            last_id = last_link.id
        except AttributeError:
            last_id = 1

        self.shortened_url = self.encode(last_id + id_digits)

        super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
