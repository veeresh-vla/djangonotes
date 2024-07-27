from rest_framework import serializers
from testapp.models import Employee
def multiples_of_1000(value):
    print('Validation by validator attribute')
    if value%1000 != 0:
        raise serializers.ValidationError('Employee salary should be multiples of 1000')
class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiples_of_1000])
    class Meta:
        model = Employee
        fields = '__all__'
