from django import forms
from app1.models import SoftwareRoles


class SoftwareForm(forms.ModelForm):
    class Meta():
        model=SoftwareRoles
        fields = '__all__'