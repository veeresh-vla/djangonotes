from django import forms
from testapp.models import Employee
class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal = self.cleaned_data['esal']
        if inputsal < 5000:
            raise forms.ValidationError('The minimum slaray should be 5000')
        return inputsal    
    class Meta:
        model = Employee
        fields = '__all__'
