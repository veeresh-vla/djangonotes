from rest_framework.serializers import ModelSerializer
from testapp.models import HydJobs
class HydJobsSerializer(ModelSerializer):
    class Meta:
        model = HydJobs
        fields = '__all__'
