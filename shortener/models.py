import string

from django.db import models
from django.utils import timezone


# Create your models here.


def timezone_delta(days: int):
    return timezone.now() + timezone.timedelta(days=days)


class Link(models.Model):
    url = models.CharField(max_length=200)
    shortened_url = models.CharField(max_length=100, editable=False)
    # TODO: make relation with User model
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now(), editable=False)
    expires_at = models.DateTimeField(
        default=timezone_delta(7), editable=False)
    expired = models.BooleanField(default=False, editable=False)

    @property
    def shortened_url(self):
        url2id = {}
        id_ = int(1e7)

        if self.url in url2id:
            id_ = url2id[self.url]
            new_url = self.encode(id_)
        else:
            url2id[self.url] = id_
            new_url = self.encode(id_)
            id_ += 1

        return f'http://www.trink/{new_url}'

    def encode(self, id_):
        '''62 chars encoder'''
        characters = string.digits + string.ascii_letters
        base = len(characters)

        result = []
        while id_ > 0:
            val = id_ % base
            result.append(characters[val])
            id_ = id_ // base

        return ''.join(result[::-1])

    def save(self, *args, **kwargs):
        shortened_url = self.shortened_url
        return super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return self.url
