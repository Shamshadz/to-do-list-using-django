from dataclasses import fields
from to_do_list.models import Create
from django import forms

class saveForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = ["title", "textarea"]