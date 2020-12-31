from rest_framework import serializers
from .models import PlacementCompanyAgents


class AgentsSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = PlacementCompanyAgents
        fields = '__all__'
        read_only_Fields = ('id',)
