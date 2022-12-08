from rest_framework import serializers

from service_first.models import Job, Status


class JobFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class StatusfullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"