from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import Link
from .serializers import LinkSerializer


class LinksView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response({'links': serializer.data})


class ShortenerView(APIView):
    def post(self, request, format=None):
        payload = {
            'url': request.query_params.get('url'),
            'created_by': request.query_params.get('created_by')
        }

        serializer = LinkSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectView(APIView):
    def get(self, request, shortened_url, format=None):
        shortened_url = self.kwargs.get('shortened_url')

        try:
            filtered_link = Link.objects.get(shortened_url=shortened_url)
            original_url = filtered_link.url
        except Link.DoesNotExist:
            context = {
                'detail': f'A URL {shortened_url} não foi encontrada ou ainda não foi encurtada.'
            }
            return Response(context)

        return HttpResponseRedirect(redirect_to=original_url)
