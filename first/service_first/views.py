from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet

from service_first.models import *
from service_first.serializers import *


class JobAPIFull(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobFullSerializer

class StatusAPIFull(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusfullSerializer
class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("work!")
