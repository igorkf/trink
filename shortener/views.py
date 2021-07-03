from rest_framework import viewsets

from .models import Link
from .serializers import LinkSerializer

# Create your views here.


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
