from django.contrib import admin

from .models import Link

# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'shortened_url', 'created_by', 'created_at', 'expires_at', 'expired')


admin.site.register(Link, LinkAdmin)
