import string
from datetime import datetime, timedelta

from django.db import models


# Create your models here.


def datetime_delta():
    return datetime.now() + timedelta(days=7)


class Link(models.Model):
    url = models.CharField(max_length=200)
    shortened_url = models.CharField(max_length=100, editable=False)
    # TODO: make relation with User model
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    expires_at = models.DateTimeField(
        default=datetime_delta, editable=False)
    expired = models.BooleanField(default=False, editable=False)

    def encode(self, id_):
        '''62 chars encoder'''
        domain = 'https://trink.com.br/'
        characters = string.digits + string.ascii_letters
        base = len(characters)

        result = []
        while id_ > 0:
            val = id_ % base
            result.append(characters[val])
            id_ = id_ // base

        return domain + ''.join(result[::-1])

    def save(self, *args, **kwargs):
        id_digits = int(1e8)
        # get last id first
        last_id = Link.objects.last().id
        self.shortened_url = self.encode(last_id + id_digits)
        super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
