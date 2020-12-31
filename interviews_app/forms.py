from django import forms
from .models import Interview
from agents_app.models import PlacementCompanyAgents


class InterviewForm(forms.Form):
    """Form with a variety of widgets to test bootstrap4 rendering."""

    date = forms.DateField(widget=forms.SelectDateWidget, required=True)
    company_name = forms.CharField(label='Company Name', max_length=255)
    logo_url = forms.URLField(label='Company logo URL')
    company_info = forms.CharField(widget=forms.Textarea)
    company_type = forms.ChoiceField(widget=forms.RadioSelect, choices=Interview.COMPANY_TYPE_CHOICES, required=True)
    company_contact_person = forms.CharField(label='Contact Person Name', max_length=255)
    company_contact_phone = forms.CharField(label='Contact Phone', max_length=31)

    placement_company_id = forms.ModelChoiceField(queryset=PlacementCompanyAgents.objects.all())
    status = forms.ChoiceField(widget=forms.Select, choices=Interview.STATUS_CHOICES, required=True)
    technology = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "CheckboxSelectMultiple"}
        ), choices=Interview.TECHNOLOGY_CHOICES,)
    position = forms.CharField(label='Position', max_length=20)
    location = forms.CharField(label='Location', max_length=255)

    required_css_class = "bootstrap4-req"

    # Set this to allow tests to work properly in Django 1.10+
    # More information, see issue #337
    use_required_attribute = False

    def clean(self):
        cleaned_data = super().clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data
