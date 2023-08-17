from django import forms


class MusicoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    edad = forms.IntegerField(required=True)
    gmail = forms.CharField(max_length=50, required=True)
    portfolio = forms.URLField(required=True)

class PintorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    edad = forms.IntegerField(required=True)
    gmail = forms.CharField(max_length=50, required=True)
    portfolio = forms.URLField(required=True)

class EscritorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    edad = forms.IntegerField(required=True)
    gmail = forms.CharField(max_length=50, required=True)
    portfolio = forms.CharField(max_length=50, required=True)