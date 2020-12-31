from rest_framework import serializers
from .models import Interview
from agents_app.serializers import AgentsSerializer
from processes_app.serializers import ProcessesSerializer


class InterviewSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""
    processes = ProcessesSerializer(many=True, read_only=True)
    placement_company = AgentsSerializer(many=False, read_only=True)
    placement_company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Interview
        fields = '__all__'
        read_only_Fields = ('id',)
        extra_fields = ['processes', 'placement_company']
