from django import forms
class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea)

    def clean(self):
        total_cleaned_data = super().clean()
        pwd = total_cleaned_data['password']
        rpwd = total_cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError('Both passwords must be same.....')
