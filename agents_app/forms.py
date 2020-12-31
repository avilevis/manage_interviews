from django import forms


class AddAgentForm(forms.Form):
    """Form with a variety of widgets to test bootstrap4 rendering."""

    placement_company_name = forms.CharField(label='Company Name', max_length=255)
    agent_name = forms.CharField(label='Agent Name', max_length=255)
    agent_phone = forms.CharField(label='Agent Phone', max_length=31)

    required_css_class = "bootstrap4-req"

    # Set this to allow tests to work properly in Django 1.10+
    # More information, see issue #337
    use_required_attribute = False

    def clean(self):
        cleaned_data = super().clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data
