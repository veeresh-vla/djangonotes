from rest_framework import viewsets
from testapp.models import HydJobs
from testapp.api.serializers import HydJobsSerializer
class HydJobsCRUDCBV(viewsets.ModelViewSet):
    queryset = HydJobs.objects.all()
    serializer_class = HydJobsSerializer
