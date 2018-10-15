from django import forms
from .models import FormModel

class Form(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = {'name','recipe','timeCook'}