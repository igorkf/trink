from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Link
from .serializers import LinkSerializer

# Create your views here.


class LinkView(APIView):
    def get(self, request, format=None):
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)

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
