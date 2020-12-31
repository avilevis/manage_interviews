from rest_framework import serializers
from .models import Processes


class ProcessesSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Processes
        fields = '__all__'
        read_only_Fields = ('id',)
