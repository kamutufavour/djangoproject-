from django import forms
from djangoProject2.model import students
class Empform(forms.ModelForm):
    class Meta:
        model=students
        fields="__all__"