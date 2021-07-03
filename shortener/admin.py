from django.contrib import admin
from .models import Link

# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Link, LinkAdmin)
