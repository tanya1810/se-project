from django import forms
from core.models import BmiMeasurement

class BmiForm(forms.Form):
    """
    height is in meters
    weight is in kg
    """
    height = forms.FloatField(label="Height in meters:", required=True, min_value=0)
    weight = forms.FloatField(label="Weight in kg:", required=True, min_value=0)

class BmiMeasurementForm(forms.ModelForm):
    class Meta:
        model = BmiMeasurement
        fields = ["id", "height_in_meters", "weight_in_kg", "measured_at"]
