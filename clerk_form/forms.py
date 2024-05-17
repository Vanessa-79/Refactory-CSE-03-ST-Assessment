from django import forms
from.models import *

class AddForm(forms.ModelForm):
    class Meta:
        model = Userform
        fields = '__all__'


date_of_birth = forms.DateField(required=True,label="",widget=forms.DateInput(attrs={'placeholder': 'date of birth (YY/MM/DD)'}))