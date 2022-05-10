from django import forms
from django.core.exceptions import ValidationError

from events.models import Conference

class EventCreationForm(forms.Form):
    class Meta:
        model = Conference
        fields = ['name', 'start_time', 'end_time', 'notes', 'con_reference', 'con_pass', 'is_active']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if end_time:
            if end_time <= start_time:
                raise forms.ValidationError("Дата окончания события должна быть позже даты его начала")

    def save(self, commit=True):
        event = super().save(commit=False)
        if commit:
            event.save()
        return event

class EventChangeForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'start_time', 'end_time', 'notes', 'con_reference', 'con_pass', 'is_active']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if end_time:
            if end_time <= start_time:
                raise forms.ValidationError("Дата окончания события должна быть позже даты его начала")