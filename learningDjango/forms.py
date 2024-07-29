from django import forms

class NumberForm(forms.Form):
    num = forms.IntegerField(label="Enter the number to check:")