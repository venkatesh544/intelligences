from django import forms

from intelligence2.models import Save


class wiproForm(forms.ModelForm):
    class Meta:
        model=Save
        fields='__all__'