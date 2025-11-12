# mathapp/forms.py
from django import forms

class PowerForm(forms.Form):
    intensity = forms.IntegerField(min_value=0, label="Intensity (I)")
    resistance = forms.IntegerField(min_value=0, label="Resistance (R)")
