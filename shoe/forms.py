from django import forms
from shoe.models import Shoes

class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = '__all__'
