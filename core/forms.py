from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field
from core.models import Waitlist

class WaitlistForm(forms.ModelForm):
    use_required_attribute = True

    class Meta:
        model = Waitlist
        fields = "__all__"
        widgets = {
          'email': forms.EmailInput(attrs={'placeholder': "Entrez votre adresse e-mail", 'type': 'email', 'class': 'bg-white w-full text-black mr-3 px-2 py-3 font-mulish rounded-lg border border-transparent focus:border-transparent focus:ring-primary'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False