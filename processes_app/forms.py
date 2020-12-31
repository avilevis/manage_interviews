from django import forms
from .models import Processes


class AddProcessForm(forms.Form):
    """Form with a variety of widgets to test bootstrap4 rendering."""

    company = forms.CharField(
        label='Company Name',
        max_length=255,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    date = forms.DateField(label='Meeting Date', widget=forms.DateInput, required=True)
    start_time = forms.TimeField(label='Meeting Time', widget=forms.TimeInput, required=True)
    duration = forms.DurationField(label='Duration')
    meeting_with = forms.CharField(label='Meeting With', max_length=255)
    meeting_content = forms.CharField(label='Contact Info', max_length=255)

    required_css_class = "bootstrap4-req"

    # Set this to allow tests to work properly in Django 1.10+
    # More information, see issue #337
    use_required_attribute = False

    def clean(self):
        cleaned_data = super().clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data
