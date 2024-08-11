from django import forms
from .models import ContactForm, KaufenForm


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = "__all__"


class KaufenFormForm(forms.ModelForm):
    class Meta:
        model = KaufenForm
        fields = "__all__"
