from django import forms
from django.core.exceptions import ValidationError
import re


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, error_messages={"error": "يجب ان يكون الاسم اقل من 30 حرف"})
    email = forms.EmailField()
    phone = forms.CharField(min_length=11)
    subject = forms.CharField(max_length=50, error_messages={"error": "يجب ان يكون الاسم اقل من 50 حرف"})
    message = forms.CharField(max_length=1500, widget=forms.Textarea(), error_messages={"error": "يجب ان يكون الاسم اقل من 1500 حرف"})

    def clean_phone(self):
        data = self.cleaned_data['phone']

        if len(str(data)) < 11:
            raise ValidationError("اقل عدد يجب ان يكون 11 رقم")
        return data
