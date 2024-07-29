from django import forms
from django.core.exceptions import ValidationError

class NumberForm(forms.Form):
    num = forms.IntegerField(label="Enter the number to check:")

    def clean_num(self):
        number = self.cleaned_data['num']
        if number < 0:
            raise ValidationError("The number must be non-negative.")
        return number
