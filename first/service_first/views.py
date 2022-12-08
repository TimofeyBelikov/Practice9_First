from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from service_first.models import *
from service_first.serializers import *


class JobAPIFull(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobFullSerializer

class StatusAPIFull(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusfullSerializer
