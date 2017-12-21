from django import forms

class SourcePathForm(forms.Form):
    path = forms.CharField(max_length=250)
