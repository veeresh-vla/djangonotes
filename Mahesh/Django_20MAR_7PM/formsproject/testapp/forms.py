from django import forms
class StudentForm(forms.Form):
    rollno = forms.IntegerField()
    name = forms.CharField()
    marks = forms.IntegerField()
