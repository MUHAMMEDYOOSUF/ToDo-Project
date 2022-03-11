from django import forms

from todoapp.models import task


class todoForms(forms.ModelForm):
    class Meta:
        model=task
        fields=['task','priority','date']



