from django.http import HttpResponseRedirect
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated

from .models import Link, EXPIRATION_DAYS, DOMAIN
from .serializers import LinkSerializer


class LinksView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        now = timezone.now() + timezone.timedelta(days=EXPIRATION_DAYS)

        links = Link.objects.filter(
            expires_at__lt=now, created_by=self.request.user.id)
        serializer = LinkSerializer(links, many=True)

        return Response({'links': serializer.data})


class ShortenerView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = {
            'url': request.data.get('url_input', ''),
            'created_by': self.request.user.id
        }

        serializer = LinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectView(APIView):
    def get(self, request, shortened_url, format=None):
        permission_classes = (IsAuthenticated,)

        shortened_url = self.kwargs.get('shortened_url')
        user_id = self.request.user.id

        try:
            filtered_link = Link.objects.filter(
                shortened_url=shortened_url, created_by=user_id).first()
            original_url = filtered_link.url
        except Link.DoesNotExist:
            context = {
                'detail': f'A URL {shortened_url} não foi encontrada ou ainda não foi encurtada.'
            }
            return Response(context)

        return HttpResponseRedirect(redirect_to=original_url)
