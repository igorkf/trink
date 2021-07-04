from rest_framework import serializers

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    shortened_url = serializers.ReadOnlyField()

    class Meta:
        model = Link
        fields = '__all__'
