from rest_framework import serializers

from .models import Link
from user.models import CustomUser


class LinkSerializer(serializers.ModelSerializer):
    shortened_url = serializers.ReadOnlyField()
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Link
        fields = '__all__'
